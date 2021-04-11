class Settings:
    location = None


class User:
    name = str()
    email = str()
    password = str()
    settings = Settings()

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

users = list()
users.append(User(name='Leonard', email='leonard@tussilago.eu', password='123'))
users.append(User(name='Ken', email='ken@tussilago.eu', password='123'))
users.append(User(name='Noelle', email='noelle@tussilago.eu', password='123'))

def get_user(name, password):
    for user in users:
        if user.name == name and user.password == password:
            return user

    return None
#
# name = input("What is your username?")
# password = input("Password?")
# user = get_user(name, password)
# if user == None:
#     print("Username or password incorrect")
# else:
#     print('Hello, ' + user.name)
