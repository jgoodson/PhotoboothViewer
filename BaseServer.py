from flask import Flask
from flask_apscheduler import APScheduler

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

app = Flask(__name__)
app.config.from_object('ConfigModule.Config')
app.debug = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    print('\n'.join(files))
    return 'test: \n'+'\n'.join(files)

app.run()

