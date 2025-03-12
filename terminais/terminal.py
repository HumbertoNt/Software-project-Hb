from users.student import student
from users.tutor import tutor
from users.master import master
from classes.turmas import *
import os

def authenticate(user_dict, username, password):
    user = user_dict.get(username)
    if user:
        user_type = type(user).__name__  # Captura a classe do usuário
        if user.login(password):
            print(f" {username} (Tipo: {user_type}) fez login com sucesso!\n")
            return user_type
        else:
            print(f" {username} (Tipo: {user_type}) tentou fazer login, mas a senha está incorreta.\n")
            return None
    print("⚠️ Usuário não encontrado!\n")
    return None

gradebook = [
    {'matricula': '0001', 'math': {'ab1': 8, 'ab2': 0}, 'science': {'ab1': 2, 'ab2': 0}},
]
a1 = classes('a1')
badu = tutor('badu', 'admin_badu', 'projeto')
aluno1 = student('joao', 'joaoPassword', 0, 'a1', 3)
aluno1.add_note('math')
aluno2 = student('arthur', 'oi', 10, 'a1', 3)
timetable1 = timetable('1A', 'vague', 'vague', 'vague', 'vague', 'vague')
a1.add_student(aluno1.name)
a1.add_student(aluno2.name)

classes_bank = {a1.classname: a1}
extra_classes_bank = {}
users_bank = {}

users_bank[aluno1.name] = aluno1
users_bank[aluno2.name] = aluno2
users_bank[badu.name] = badu

class terminal:
    def __init__(self):
        pass  # Inicializa sem estudante logado

    def run(self):
        """Executa o loop principal do sistema."""
        while True:
            if not self.portal():
                break

    def portal(self):
        while True:
            self.clear()
            name_user = input('Name: ')
            password_user = input('Password: ')
            if authenticate(users_bank, name_user, password_user) == None:
                choice = input('quit?(y/n) ')
                match choice.lower():
                    case 'y':
                        return False
                    case 'n':
                        pass
            elif authenticate(users_bank, name_user, password_user) == 'tutor':
                self.clear()
                self.tutor()
            elif authenticate(users_bank, name_user, password_user) == 'student':
                self.clear()
                self.student(users_bank[name_user].name)

# -----------------Tutor portal-----------------
    def tutor(self):
        while True:
            print()
            print('Press 0 for quit')
            print('Press 1 for enroll students')
            print('Press 2 for daily attendance')
            print('Press 3 for create a class')
            print('Press 4 for timetable manage')
            print('Press 5 for add exam')
            print('Press 6 for add matter in gradebook')
            print('Press 7 for edit gradebook')
            print('Press 8 for creat a new extra class.')
            print('Press 9 for add studient a new extra class.')

            choice = input('action: ')
            match choice:
                case '0':
                    return False  # Sai do menu tutor e volta ao portal
                case '1':
                    self.clear()
                    self.enroll_students()
                case '2':
                    self.clear()
                    self.attendance()
                case '3':
                    self.clear()
                    self.create_class()
                case '4':
                    self.clear()
                    class_name = input('Class name: ')
                    classes_bank[class_name].edit()
                case '5':
                    self.clear()
                    class_name = input('Class name: ')
                    exam_matter = input('Exam matter: ')
                    exam_date = input('Exam date: ')
                    classes_bank[class_name].add_exams(exam_matter, exam_date)
                case '6':
                    self.clear()
                    student_name = input('Student name:')
                    matter_name = input('Matter name: ')
                    users_bank[student_name].add_note(matter_name)
                case '7':
                    self.clear()
                    student_name = input('Student name:')
                    matter_name = input('Matter name: ')
                    users_bank[student_name].edit_note(matter_name)
                case '8':
                    name_extra_class = input('Name extra class: ')
                    new_class = classes(name_extra_class)
                    extra_classes_bank[name_extra_class] = new_class
                case '9':
                    name_extra_class = input('Name extra class: ')
                    if name_extra_class in extra_classes_bank:
                        student_name = input('Student name: ')
                        if student_name in users_bank:
                            extra_classes_bank.add_student(student_name)
                        else:
                            print('Student not found')
                    else:
                        print('Class not found')
                case _:
                    self.clear()
                    print('Invalid option')

    def enroll_students(self):
        new_name = input('Student name: ')
        while True:
            new_classe = input('Class: ')
            if new_classe in classes_bank:
                break
            else:
                print('Class not found')
        new_installments = int(input('installments paid: '))
        new_password = '0000'
        new_student = student(new_name, new_password, 0, new_classe, 12 - new_installments)
        users_bank[new_name] = new_student
        classes_bank[new_classe].add_student(new_name)
        new_student.show()

    def attendance(self):
        name_class = input('Name class: ')

        if name_class not in classes_bank:
            print("Class not found!")
            return

        print(classes_bank[name_class].students)

        for student_name in classes_bank[name_class].students:  # Iterando diretamente sobre nomes dos alunos
            print(users_bank[student_name].name)
            absence = input('Present? yes(1) or no (0)? ')
            users_bank[student_name].daily_attendance(absence)


    def create_class(self):
        new_classename = input('Class name: ')
        new_classe = classes(new_classename)
        classes_bank[new_classename] = new_classe

# ----------------Student portal----------------
    def student(self, code):
        while True:
            print('Press 0 for quit')
            print('Press 1 for see informations')
            print('Press 2 for see gradebook')
            print('Press 3 for edit password')

            choice = input('action: ')
            match choice:
                case '0':
                    self.clear()
                    break  # Sai do menu aluno e volta ao portal
                case '1':
                    self.clear()
                    users_bank[code].show()
                case '2':
                    self.clear()
                    users_bank[code].show_note()
                case '3':
                    self.clear()
                    new_password = input('New password: ')
                    users_bank[code].edit_password(new_password)
                case _:
                    self.clear()
                    print('Invalid option')
# ---------------------------------------------- 
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
