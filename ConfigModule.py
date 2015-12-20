class Config(object):
    JOBS = [
        {
            'id': 'watch_folder',
            'func': 'FileWatcher:watch_folder',
            'args': ('c:/Users/jonathan/Pictures/PhotoBooth/', '.jpg'),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True