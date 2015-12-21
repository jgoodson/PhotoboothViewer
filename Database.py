from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import StaticPool

#TODO break out database details into config file
engine = create_engine('sqlite:///photos.db',
                       connect_args={'check_same_thread': False},
                       poolclass=StaticPool)

Base = declarative_base()

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    time = Column(DateTime)

    def __repr__(self):
        return "Photo(filename='{}', id={}, time='{}'".format(self.filename, self.id, self.time)

Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)