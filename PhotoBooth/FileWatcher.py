import os

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.delete('files')

def watch_folder(folder):
    existing = r.smembers('files')
    for file in os.listdir(folder):
        pass