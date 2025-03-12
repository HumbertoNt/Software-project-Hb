from users.user import user

class tutor(user):
    def __init__(self, name, password, matter):
        super().__init__(name, password)
        self.__matter = matter
    
    def login(self, password):
        return password == self._password
    
    def edit_password(self, new_password):
        self._password = new_password
        print('Password changed')

    @property
    def matter(self):
        return self.__matter
 