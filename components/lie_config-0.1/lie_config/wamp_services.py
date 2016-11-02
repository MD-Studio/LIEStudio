# -*- coding: utf-8 -*-

"""
file: wamp_services.py

WAMP service methods the module exposes.
"""

import time
import json

from   autobahn               import wamp
from   twisted.internet.defer import inlineCallbacks

from   lie_system import LieApplicationSession
from   lie_config import get_config

class ConfigWampApi(LieApplicationSession):
    """
    Configuration management WAMP methods.
    """
       
    @wamp.register(u'liestudio.config.get')
    def getConfig(self, key, config='default'):
        """
        Retrieve application configuration.
    
        Search for `key` anywhere in a globally accessible 
        configuration store. 
        Returns query results in JSON format
        """
        
        settings = self.package_config.search('*{0}*'.format(str(key)))
        return settings.dict(nested=True)

def make(config):
    """
    Component factory
  
    This component factory creates instances of the application component
    to run.
    
    The function will get called either during development using an 
    ApplicationRunner, or as a plugin hosted in a WAMPlet container such as
    a Crossbar.io worker.
    The LieApplicationSession class is initiated with an instance of the
    ComponentConfig class by default but any class specific keyword arguments
    can be consument as well to populate the class session_config and
    package_config dictionaries.
    
    :param config: Autobahn ComponentConfig object
    """
    
    if config:
        return ConfigWampApi(config)
    else:
        # if no config given, return a description of this WAMPlet ..
        return {'label': 'LIEStudio configuration management WAMPlet',
                'description': 'WAMPlet proving LIEStudio configuration management endpoints'}