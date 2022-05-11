from Utils.utils import Base
from sqlalchemy import Column, String, Date, Float


class UserDeposits(Base):
    __tablename__ = 'user_deposits'

    user_id = Column(String(13), primary_key=True)
    username = Column(String(30))
    user_password_hash = Column(String(25))
