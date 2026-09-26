import re
import logging
import hashlib
import sys

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")


def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

class Authorization:
    def start(self):
        logging.info("Запущена функция запроса данных для регистрации")

        login = input("Введите логин:")
        password = input("Введите пароль:")
        check_password = input("Введите пароль повторно:")

        logging.info("Данные получены")

        result = self.validation(login, password, check_password)

        logging.info("Вывод результатов")

        print(result[0])
        print(result[1])

        if result[0]:
            logging.info(f"Логин: {login}, Пароль: {hash_password(password)} | Регистрация успешна завершена")
        else:
            logging.error(f"Логин: {login}, Пароль: {hash_password(password)} | Ошибка: {result[1]}")

    def validation(self,login,password,check_password):
        logging.info("Запуск проверки на валидацию")
        try:
            logging.info("Проверка валидации логина")
            check_login = self.checkLogin(login)

            logging.info("Проверка валидации пароля")
            check_password = self.checkPassword(password,check_password)

            logging.info(f"Валидация успешна пройдена")
            return True,""
        except ValueError as e:
            logging.error(f"Валидация не пройдена")
            return False,e

    def checkLogin(self,login):
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


    def checkPassword(self,password,check_password):
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
auth.start()