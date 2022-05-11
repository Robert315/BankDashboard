class UsersAccountsController:
    def __init__(self, user_accounts_repo):
        self.users_accounts_repo = user_accounts_repo

    def check_balance_exceeds(self, user_id, amount, currency):
        user_account = self.users_accounts_repo.read_with_currency(user_id, currency)
        if user_account and user_account.amount > amount:
            return True

        return False

    def transfer_amount(self, user_id, amount, currency):
        total_amount = self.users_accounts_repo.read_with_currency(user_id, currency).amount
        self.users_accounts_repo.update(user_id, currency, total_amount - amount)

    def add_amount(self, user_id, amount, currency):
        total_amount = self.users_accounts_repo.read_with_currency(user_id, currency).amount
        self.users_accounts_repo.update(user_id, currency, total_amount + amount)

    def check_account(self, user_id, currency):
        res = self.users_accounts_repo.read_with_currency(user_id, currency)
        if res:
            return True
        return False
