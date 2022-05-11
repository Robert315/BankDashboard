class UsersController:
    def __init__(self, user_repo):
        self.user_repo = user_repo


    def get_user_info(self, user_id):
        return self.user_repo.read(user_id)

