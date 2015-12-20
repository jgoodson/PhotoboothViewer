from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Photo(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    time = Column(DateTime)

    def __repr__(self):
        return "<Photo(filename='{}', id={}, time='{}'".format(self.filename, self.id, self.time)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)