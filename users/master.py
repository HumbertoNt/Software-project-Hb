from users.user import user

class master(user):
    def __init__(self, name, password):
        super().__init__(name, password)

    def login(self, password):
        if password == self.__password:
            return 1
        else:
            return 0
        
    def edit_password(self, new_password):
        self.__password = new_password
        print('Password changed')

    @property
    def name(self):
        return self.__name