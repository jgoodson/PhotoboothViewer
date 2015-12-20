import os
import os.path

from Database import Session, Photo


def watch_folder(folder):
    files = os.listdir(folder)
    session = Session()
