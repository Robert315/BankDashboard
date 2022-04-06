from sqlalchemy.orm import sessionmaker
from Model.Domain.users_Accounts import UsersAccounts
from Utils.utils import engine, Base


class UserAccountsRepository:

    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, account_number, currency, amount):
        new_user_account = UsersAccounts(
            user_id=user_id,
            account_number=account_number,
            currency=currency,
            amount=amount
        )

        self.session.add(new_user_account)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(UsersAccounts).filter_by(user_id=user_id).all()

    def read_with_currency(self, user_id, currency):
        return self.session.query(UsersAccounts).filter_by(user_id=user_id, currency=currency).first()

    def update(self, user_id, currency, amount):
        if amount:
            self.session.query(UsersAccounts).filter_by(user_id=user_id, currency=currency).update({'amount': amount})

    def delete(self, user_id):
        self.session.query(UsersAccounts).filter_by(user_id=user_id).delete()
        self.session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UserAccountsRepository()
    repo.create('1234567890123', '123456789012345678901234', 'EUR', 100.45)
