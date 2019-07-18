
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Sequence
from sqlalchemy.types import (
    Integer,
    String,
)


base = declarative_base()

TABLE_ID = Sequence('account_table_id_seq', start=1000)


class Account(base):
    __tablename__ = 'account'

    id = Column(Integer, TABLE_ID, primary_key=True, server_default=TABLE_ID.next_value())
    account_id = Column(UUID(as_uuid=True), default=uuid4, index=True, unique=True)
    username = Column(String, unique=True)
