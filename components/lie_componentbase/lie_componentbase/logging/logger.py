import threading
import copy
import sys
import os

from datetime import datetime
from twisted.python import log
from zope.interface import provider, implementer
from twisted.python import logfile
from twisted.internet import reactor
from autobahn.wamp.exception import ApplicationError
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from twisted.python.failure import Failure
from twisted.logger import (ILogObserver, ILogFilterPredicate, PredicateResult, LogLevel,
                            globalLogPublisher, Logger, FilteringLogObserver, LogLevelFilterPredicate)

from ..config import PY3

if PY3:
    from queue import Queue, Empty
else:
    from Queue import Queue, Empty


def block_on(d, timeout=None):
    q = Queue()
    d.addBoth(q.put)
    try:
        ret = q.get(timeout is not None, timeout)
    except Empty:
        raise TimeoutError
    if isinstance(ret, Failure):
        ret.raiseException()
    else:
        return ret

LOGLEVELS = ['debug', 'info', 'warn', 'error', 'critical']

class PrintingObserver:
    """
    ILogObserver that writes formatted log events to stdout or stderr

    :param out:          Output stream as sys.stdout or sys.stderr
    :type out:           File object representing Python interpreter standard
                         output or error stream
    :param format_event: Format string suitable for parsing using the Formatter
                         class (Python format buildin). The log event dictionary
                         is passed to the format function.
    :type format_event:  String with optional format replacement fields
    :param datefmt:      Date and time format string following strftime convention
    :type datefmt:       string
    """

    def __init__(self, out, namespace = None, **kwargs):
        self._out = open(out, 'w') if out == os.devnull else out

        self.format_event = '{asctime} - [{log_level.name:<5}: {log_namespace}] - {message}\n'
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.namespace = namespace

    def __call__(self, event):
        """
        Evaluate event dictionary, format the log message and
        write to output stream

        :param event: Twisted logger event
        :type event : dict
        """
        if self.namespace and not event['log_namespace'] == self.namespace:
            return

        if event.get('log_format', None):
            message = event['log_format'].format(**event)
        else:
            message = event.get('message', '')

        oldMsg = event.pop('message')

        self._out.write(self.format_event.format(asctime=datetime.fromtimestamp(event['log_time']).strftime(self.datefmt), 
                                                  message=message, 
                                                  **event))

        if oldMsg:
            event['message'] = oldMsg

class WampLogObserver(object):

    def __init__(self, session, min_level='info'):
        self.format_event = '{asctime} - [{log_level.name:<5}: {log_namespace}] - {message}\n'

        self.session = session
        self.namespace = self.session.component_info.get('namespace')
        self.min_level_index = LOGLEVELS.index(min_level)
        self.log_queue = Queue()
        self.shutdown = False

    def __call__(self, event):
        level = event.get("log_level", None)
        if level is None:
            levelName = u"-"
        else:
            levelName = level.name

        if event.get('log_format', None):
            message = event['log_format'].format(**event)
        else:
            message = event.get('message', '')

        if LOGLEVELS.index(levelName) >= self.min_level_index and event['log_namespace'] == self.namespace:
            logstruct = {
                'level': level,
                'namespace': self.session.component_info['namespace'],
                'user': self.session.session_config.get('authid', self.session.session_config.get('role', 'anonymous')),
                'time': event['log_time'],
                'message': message
            }

            self.log_queue.put(logstruct)

    def start_flushing(self):
        self.session.log.info('Start wamp logging')
        self.log_list = []
        reactor.callLater(0.1, self._flush)
    
    @inlineCallbacks
    def _flush(self):        
        while not self.log_queue.empty() and len(self.log_list) < 50:
            self.log_list.append(self.log_queue.get(timeout=0.1))

        if len(self.log_list) >= 50 or (len(self.log_list) > 0 and self.shutdown):
            self.session.log.info('Log list full, flushing')
            try:
                res = yield self.session.call(u'liestudio.logger.log', {'namespace': self.namespace, 'logs': self.log_list})
            except ApplicationError:
                yield sleep(1)
            else:
                self.log_list = []                

        if not self.shutdown:
            # enqueue again
            reactor.callLater(2, self._flush)
        elif not self.log_queue.empty() or not len(self.log_list) == 0:
            while not self.log_queue.empty():
                self.log_list.append(self.log_queue.get())

            yield self.session.call(u'liestudio.logger.log', {'namespace': self.namespace, 'logs': self.log_list})
            self.log_list = []
            
