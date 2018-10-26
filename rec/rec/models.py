from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import (
    Integer,
    String,
)

base = declarative_base()


class Account(base):
     __tablename__ = 'account'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     password = Column(String)

     def __repr__(self):
        return "<Account(name='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)
