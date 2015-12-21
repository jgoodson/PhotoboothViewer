from datetime import datetime
import ujson

from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
from sqlalchemy import not_

from Database import Session, Photo

from time import time

app = Flask(__name__)
#app.config.from_object('ConfigModule.Config')
app.debug = True


@app.route('/')
def index():
    session = Session()
    return '<p>'+'<br>'.join(str(_) for _ in session.query(Photo))+'</p>'


@app.route('/test')
def test_gallery():
    session = Session()
    photos = [p for p in session.query(Photo).order_by(Photo.time.desc())]
    Session.remove()
    return render_template('GalleryTemplate.html', photos=[p.filename for p in photos], indices=[p.id for p in photos])


@app.route('/get_updates')
def fetch(*args, **kwargs):
    known_indices = ujson.loads(request.query_string)
    session = Session()
    new_photos = session.query(Photo).filter(not_(Photo.id.in_(known_indices))).order_by(Photo.time).all()
    print(new_photos)
    return ujson.dumps({'ids': [p.id for p in new_photos],
                        'filenames': [p.filename for p in new_photos]})


if __name__ == '__main__':
    app.run()

