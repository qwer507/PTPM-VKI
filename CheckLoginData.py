import re

class Authorization:
    def Start(self):
        login = input("Введите логин:")
        password = input("Введите пароль:")
        check_password = input("Введите пароль повторно:")
        result = self.Validation(login, password, check_password)
        print(result[0])
        print(result[1])

    def Validation(self,login,password,check_password):
        try:
            check_login = self.CheckLogin(login)
            check_password = self.CheckPassword(password,check_password)
            return True,""
        except ValueError as e:
            return False,e

    def CheckLogin(self,login):
        black_list = ("admin","manager","user")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        phone_regex = r"^\+\d-\d{3}-\d{3}-\d{4}$"
        login_regex = r"^[a-zA-Z0-9_]+$"
        if re.match(email_regex, login) or re.match(phone_regex, login):
            return True
        if len(login) < 5:
            raise ValueError("Логин должен быть из пяти или больше символов")
        if not re.match(login_regex, login):
            raise ValueError("Логин должен содержать только латинские буквы, цифры и нижнее подчеркивание")
        if login in black_list:
            raise ValueError("Этот логин нельзя использовать")
        return True


    def CheckPassword(self,password,check_password):
        password_regex = r"^[а-яёА-ЯЁ0-9\W_]+$"
        upper_regex = r"[А-ЯЁ]"
        lower_regex = r"[а-яё]"
        symbol_regex = r"[\W_]"
        number_regex = r"[0-9]"
        if len(password) < 7:
            raise ValueError("Пароль должен быть из семи или больше символов")
        if not re.match(password_regex,password):
            raise ValueError("Пароль должен содержать только кириллицу, цифры и спецсимволы")
        if not re.search(upper_regex,password):
            raise ValueError("Пароль должен содержать хотя бы одну букву в верхнем регистре")
        if not re.search(lower_regex,password):
            raise ValueError("Пароль должен содержать хотя бы одну букву в нижнем регистре")
        if not re.search(number_regex,password):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not re.search(symbol_regex,password):
            raise ValueError("Пароль должен содержать хотя бы один спецсимвол")
        if check_password != password:
            raise ValueError("Пароли не совпадают")
        return True


auth = Authorization()
auth.Start()