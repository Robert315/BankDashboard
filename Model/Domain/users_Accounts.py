from Utils.utils import Base
from sqlalchemy import Column, String, Float, ForeignKey

class UsersAccounts(Base):
    
    __tablename__ = 'usersaccounts'

    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    account_number = Column(String(24))
    currency = Column(String(3))
    amount = Column(Float(2))
  