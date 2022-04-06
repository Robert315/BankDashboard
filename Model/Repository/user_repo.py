from sqlalchemy.orm import sessionmaker
from datetime import datetime
from Model.Domain.users import Users
from Utils.utils import engine, Base


class UsersRepository:

    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, user_id, first_name, last_name, email, address, phone_number, date_of_birth):
        new_user = Users(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            join_date=datetime.now()
        )
        self.session.add(new_user)
        self.session.commit()

    def read(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()

    def update(self, user_id, **kwargs):
        print(kwargs)
        self.session.query(Users).filter_by(user_id=user_id).update({'first_name': val})

    def delete(self, user_id):
        self.session.query(Users).filter_by(user_id=user_id).delete()
        self.session.commit()

    def read_all(self):
        return self.session.query(Users).all()

    def get_email_by_user_id(self, user_id):
        return self.session.query(Users).filter_by(user_id=user_id).first()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    repo = UsersRepository()
    repo.create('1234567890123', 'Robert', 'Nicolau', 'robert@yahoo.ro', 'adress1', '0734728099', datetime.now())
