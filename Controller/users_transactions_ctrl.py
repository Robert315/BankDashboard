class UsersTransactionsController:
    def __init__(self, user_transactions_repo):
        self.user_transactions_repo = user_transactions_repo

    def add_transaction(self, user_id, amount, currency, vendor):
        self.user_transactions_repo.create(user_id, amount, currency, vendor)
