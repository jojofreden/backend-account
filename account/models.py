from sqlalchemy import Column, String, Binary

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import (
    Integer,
    String,
)

base = declarative_base()


class Account(base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    username = Column(String)
