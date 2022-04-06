from Utils.utils import Base
from sqlalchemy import Column, Integer, CHAR, TEXT, BOOLEAN
from datetime import date


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    user_id = Column(CHAR(13))
    messages = TEXT
    date = date
    state = BOOLEAN
