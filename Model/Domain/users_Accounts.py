from Utils.utils import Base
from sqlalchemy import Column, Float,CHAR, String


class UsersAccounts(Base):
    __tablename__ = 'usersaccounts'

    user_id = Column(String(13), primary_key=True)
    account_number = Column(CHAR(24))
    currency = Column(String(3))
    amount = Column(Float(2))
