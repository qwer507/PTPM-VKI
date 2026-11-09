import re

class PasswordValidator:
    def validator_password(self, password: str):
        if type(password) != str:
            raise TypeError("Пароль должен быть строкой")
        if password.find(" ") != -1:
            raise ValueError("Пароль не должен содержать пробелы")

        upper_regex = r"[А-ЯЁ]"
        lower_regex = r"[а-яё]"
        symbol_regex = r"[!@#$%^&*]"
        number_regex = r"[0-9]"
        if len(password) < 8 or len(password) > 20:
            return False
        if not re.search(upper_regex, password):
            return False
        if not re.search(lower_regex, password):
            return False
        if not re.search(number_regex, password):
            return False
        if not re.search(symbol_regex, password):
            return False
        return True



