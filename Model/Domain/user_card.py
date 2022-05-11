from Utils.utils import Base
from sqlalchemy import Column, String, DATE


class UserCard(Base):
    __tablename__ = 'user_card'

    user_id = Column(String(13), primary_key=True)
    card_number = Column(String(16), primary_key=True)
    pin_hash = Column(String(256))
    cvv = Column(String(256))
    expiration_date = DATE()
