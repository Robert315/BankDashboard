from Utils.utils import Base,engine
from sqlalchemy import Column, String, Float, ForeignKey, Integer,DateTime


class UsersTransactions(Base):
    
    __tablename__ = 'userstransaction'

    transaction_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(String(13), primary_key=True, foreign_key=ForeignKey('users.user_id', ondelete='CASCADE'))
    currency = Column(String(3))
    amount = Column(Float(2))
    vendor = Column(String(100))
    date_time = Column(DateTime)

    def __repr__(self):
        return f'<{self.transaction_id}, {self.user_id}, {self.currency},{self.amount}, {self.vendor}, {self.date_time}>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UserTransactionsRepository()