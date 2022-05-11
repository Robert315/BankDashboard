from Controller.users_accounts_ctrl import UsersAccountsController
from Controller.users_ctrl import UsersController
from Controller.users_transactions_ctrl import UsersTransactionsController
from Model.Repository.user_accounts_repo import UserAccountsRepository
from Model.Repository.user_repo import UsersRepository


class AppController:
    def __init__(self, users_ctrl, users_accounts_ctrl, users_transactions_ctrl):
        self.users_ctrl = users_ctrl
        self.users_accounts_ctrl = users_accounts_ctrl
        self.users_transactions_ctrl = users_transactions_ctrl

    def create_transaction(self, user_id, amount, currency, vendor):
        if self.users_accounts_ctrl.check_balance_exceeds(user_id, amount, currency):
            self.users_accounts_ctrl.transfer_amount(user_id, amount, currency, vendor)
            self.users_transactions_ctrl.add_transaction(user_id, amount, currency, vendor)
            return True

        return False

    def users_info(self, user_id):
        first_user = self.users_ctrl.get_user_info(user_id)
        user_json = {
            'user_id': first_user.user_id,
            'first_name': first_user.first_name,
            'last_name': first_user.last_name,
            'email': first_user.email,
            'address': first_user.address,
            'phone_number': first_user.phone_number,
            'date_of_birth': first_user.date_of_birth,
            'join_date': first_user.join_date
        }
        return user_json

    def add_money(self, user_id, amount, currency):
        if self.users_accounts_ctrl.check_account(user_id, currency):
            self.users_accounts_ctrl.add_amount(user_id, amount, currency)
            return True
        return False



if __name__ == '__main__':
    users_repo = UsersRepository()
    users_accounts_repo = UserAccountsRepository()
    users_transactions_repo = UsersRepository()

    users_ctrl = UsersController(users_repo)
    users_accounts_ctrl = UsersAccountsController(users_accounts_repo)
    users_transactions_ctrl = UsersTransactionsController(users_transactions_repo)

    app_ctrl = AppController(users_ctrl, users_accounts_ctrl, users_transactions_ctrl)

    # res = app_ctrl.create_transaction('1234567890123', 1000, 'EUR', 'Emag', 'Shopping')
    res = app_ctrl.users_info('1234567890123')
    print(res)