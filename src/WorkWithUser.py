import abc

class UserInteraction(abc.ABC):
    @abc.abstractmethod
    def getData(self):
        pass

class WorkWithUser(UserInteraction):
    def getData(self):
        login = input("Введите логин:")
        password = input("Введите пароль:")
        check_password = input("Введите пароль повторно:")

        return login, password, check_password
