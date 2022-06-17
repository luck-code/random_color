from app import db
from sqlalchemy import Column, Integer, String


class Developments(db.Model):
    id = Column(Integer, primary_key=True)
    blue = Column(String(10))
    green = Column(String(10))
    red = Column(String(10))
    color = Column(String(10))
    number = Column(Integer)
    box = Column(String(1000))

