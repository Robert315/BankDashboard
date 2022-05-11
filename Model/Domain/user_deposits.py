from Utils.utils import Base
from sqlalchemy import Column, String, Float


class UserDeposits(Base):
    __tablename__ = 'user_deposits'

    user_id = Column(String(13), primary_key=True)
    currency = Column(String(3))
    depo_name = Column(String(50))
    amount = Column(Float(2))
    description = Column(String(200))