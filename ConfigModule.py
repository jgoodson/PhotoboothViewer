class Config(object):
    JOBS = [
        {
            'id': 'watch_folder',
            'func': 'FileWatcher:watch_folder',
            'args': ('/Users/jonathan/Pictures/PhotoBooth/',),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True