from users.user import user

class student(user):
    def __init__(self, name, password, absence, classe, installment):
        super().__init__(name, password)
        self.__absence = int (absence)
        self.__classe = classe
        self.__installment = int (installment)
        self.__gradebook = {}
    
    def login(self, password):
        return password == self._password
    
    def edit_password(self, new_password):
        self._password = new_password
        print('Password changed')
    
    def daily_attendance(self, present):
        if present == '1':
            print("present!")
        elif present == '0':
            print("absence")
            self.__absence += 1

    def show(self):
        print()
        print('Name:', self._name)
        print('absence:', self.__absence)
        print('Class:', self.__classe)
        print('Remaining installments:', 12 - self.__installment)

    def add_note(self, matter_name):
        matter = note(matter_name, 0, 0)
        self.__gradebook[matter_name] = matter
        self.__gradebook[matter_name].show()
    
    def edit_note(self, matter):
        self.__gradebook[matter].show()
        choice = input('quit(0), ab1(1) or ab2(2)')
        match choice:
            case '0':
                return
            case '1':
                self.__gradebook[matter].edit(1)
            case '2':
                self.__gradebook[matter].edit(2)
    def show_note(self):
        for matter in self.__gradebook:
            self.__gradebook[matter].show()


class note:
    def __init__(self, matter, ab1, ab2):
        self.__matter = matter
        self.__ab1 = int (ab1)
        self.__ab2 = int (ab2)
    def show(self):
        print(f'Matter: {self.__matter}')
        print(f'Ab1: {self.__ab1}')
        print(f'Ab2: {self.__ab2}')
        print(f'Average: {(float(self.__ab1) + float(self.__ab2)) / 2}')
    def edit(self, num):
        if num == 1:
            new_ab1 = input('ab1 new note: ')
            self.__ab1 == new_ab1
        elif num == 2:
            new_ab2 = input('ab2 new note: ')
            self.__ab2 == new_ab2
