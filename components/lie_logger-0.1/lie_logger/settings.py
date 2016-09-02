settings = {
  'PrintingObserver': {
    'activate': True,
    'datefmt': '%m/%d/%Y %I:%M:%S',
    'format_event': '{asctime} - [{log_level.name:<5}: {log_namespace}] - {message}\n',
    'filter_predicate': {'log_level':'debug', 'app_namespace':' > 5'}
  },
  'ExportToMongodbObserver': {
    'activate': True,
    'log_cache_size': 50,
  },
  'RotateFileLogObserver': {
    'activate': True,
    'datefmt': '%m/%d/%Y %I:%M:%S',
    'format_event': '{asctime} - [{log_level.name:<5}: {log_namespace}] - {message}\n',
    'logfile_path': '/Users/mvdijk/Documents/WorkProjects/liestudio-master/liestudio/data/logs/lielog.log',
    'rotation_time': 86400
  },
}