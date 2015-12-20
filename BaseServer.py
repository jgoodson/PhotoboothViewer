from datetime import datetime

from flask import Flask, render_template
from flask_apscheduler import APScheduler

from Database import Session, Photo

from time import time

app = Flask(__name__)
app.config.from_object('ConfigModule.Config')
app.debug = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def index():
    session = Session()
    return '<p>'+'<br>'.join(str(_) for _ in session.query(Photo))+'</p>'

@app.route('/test')
def test_gallery():
    session = Session()
    return render_template('GalleryTemplate.html', photos=list(reversed([p[0] for p in session.query(Photo.filename).all()])))
    Session.remove()

app.run()

