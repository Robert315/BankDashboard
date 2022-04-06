
from Utils.utils import Base
from sqlalchemy import Column, String, Integer, Date 

class Users(Base):
    
    __tablename__ = 'users'

    user_id = Column(String(13), primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50))
    address = Column(String(200))
    phone_number = Column(String(10))
    date_of_birth = Column(Date)
    join_date = Column(Date)
