import subprocess
import os

import ujson

from flask import Flask, render_template, request

from sqlalchemy import not_

from Database import Session, Photo


app = Flask(__name__)

app.debug = True


@app.route('/')
def index():
    session = Session()
    s = '<p>'+'<br>'.join(str(_) for _ in session.query(Photo))+'</p>'
    session.close()
    return s


@app.route('/test')
def test_gallery():
    session = Session()
    photos = [p for p in session.query(Photo).order_by(Photo.time.desc())]
    output = render_template('GalleryTemplate.html', photos=[p.filename for p in photos], indices=[p.id for p in photos])
    session.close()
    return output


@app.route('/get_updates')
def fetch(*args, **kwargs):
    known_indices = ujson.loads(request.query_string)
    session = Session()
    new_photos = session.query(Photo).filter(not_(Photo.id.in_(known_indices))).order_by(Photo.time).all()
    return ujson.dumps({'ids': [p.id for p in new_photos],
                        'filenames': [p.filename for p in new_photos],
                        })

@app.route('/get_comments')
def get_comments():
    session = Session()
    image_name = request.query_string.decode('UTF-8')
    print(image_name)
    image = session.query(Photo).filter_by(filename=image_name).first()
    comments = image.comments
    session.close()
    return comments


@app.route('/update_comments', methods=['PUT'])
def update_comments():
    image_name = os.path.basename(request.form.get('imagename'))
    comments = request.form.get('comments')
    print(image_name, comments)
    session = Session()
    image = session.query(Photo).filter_by(filename=image_name).first()
    image.comments = comments
    session.commit()
    session.close()
    return "Updated"


@app.route('/print')
def print_command(*args, **kwargs):
    filename = os.path.basename(request.query_string[3:-3]).decode('UTF-8')
    print("called print_command with {}".format(filename))
    if filename in os.listdir('/Users/jonathan/Pictures/PhotoBooth'):
        print_photo('/Users/jonathan/Pictures/PhotoBooth/{}'.format(filename))
        return "Good!"

def print_photo(image_name):
    subprocess.call(['lpr', '-P', 'EPSON_PictureMate_PM_225', '{}'.format(image_name)])

if __name__ == '__main__':
    app.run()

