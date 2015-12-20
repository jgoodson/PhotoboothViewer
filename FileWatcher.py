import os
import os.path

from datetime import datetime

from Database import Session, Photo

from PIL import Image


def watch_folder(folder, ext, thumb_size=(400, 200)):
    files = set(p for p in os.listdir(folder) if p.lower().endswith(ext))
    session = Session()
    existing = set(i[0] for i in session.query(Photo.filename).all())
    new = files.difference(existing)
    new_entries = []
    for photo in new:
        im = Image.open(folder+photo)
        im.save('static/images/'+photo)
        im.thumbnail(thumb_size, Image.ANTIALIAS)
        im.save('static/thumbnails/'+photo)
        new_entries.append(Photo(filename=photo, time=datetime.fromtimestamp(os.path.getmtime(folder+photo))))
    session.add_all(new_entries)
    session.commit()
    Session.remove()