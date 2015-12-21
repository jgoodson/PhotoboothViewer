import os
import os.path
from datetime import datetime

from PIL import Image
from apscheduler.schedulers.background import BlockingScheduler

from Database import Session, Photo


def watch_folder(folder, ext, thumb_size=(400, 200)):
    files = set(p for p in os.listdir(folder) if p.lower().endswith(ext))
    session = Session()
    existing = set(i[0] for i in session.query(Photo.filename).all())
    new = files.difference(existing)
    for photo in new:
        im = Image.open(folder+photo)
        im.save('static/images/'+photo)
        im.thumbnail(thumb_size, Image.ANTIALIAS)
        im.save('static/thumbnails/'+photo)
        session.add(Photo(filename=photo, time=datetime.fromtimestamp(os.path.getmtime(folder+photo))))
        session.commit()

    Session.remove()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    #TODO move this info to config file
    scheduler.add_job(watch_folder, 'interval', args=(
        'c:/Users/jonathan/Pictures/PhotoBooth/',
        '.jpg',
    ), seconds=1)
    scheduler.start()