from datetime import datetime

from flask import Flask
from flask_apscheduler import APScheduler

from Database import Session, Photo

app = Flask(__name__)
app.config.from_object('ConfigModule.Config')
app.debug = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    print('\n'.join())
    return 'test: \n'+'\n'.join()
session = Session()
wakka = Photo(filename='wakka.txt', time=datetime.now())
session.add(wakka)
session.commit()

print("LOOK AT ME: \n", session.query(Photo).all())
app.run()

