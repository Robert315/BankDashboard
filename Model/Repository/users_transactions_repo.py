
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from Model.Domain.users_transactions import UsersTransactions
from Utils.utils import engine, Base

class UserTransactionsRepository:

    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, currency, amount, vendor):

        new_user_transactions = UsersTransactions(
            user_id=user_id,
            currency=currency,
            amount=amount,
            vendor=vendor,
            date_time=datetime.now()
        )

        self.session.add(new_user_transactions)
        self.session.commit()


    def read_all(self, user_id):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id).all()
    
    def read_with_currency(self, user_id, currency):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id, currency=currency).all()
    
    def read_with_currency(self, user_id, vendor):
        return self.session.query(UsersTransactions).filter_by(user_id=user_id, currency=vendor).all()
    
    def delete(self, user_id, date_time):
        
        self.session.query(UsersTransactions).filter_by(user_id=user_id, date_time=date_time).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UserTransactionsRepository()
    repo.create('1234567890123', 'EUR', 100.23, 'Emag')
