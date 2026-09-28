import unittest
from src.CheckLoginData import Authorization

class TestAuthorization(unittest.TestCase):
    CORRECT_LOGIN = "rwfwiurnj"
    CORRECT_PASSWORD = "акцацкВ1!"

    def setUp(self):
        self.auth = Authorization()

    def tearDown(self):
        self.auth = None

    def test_email_login(self):
        login = "saddagwr@mail.ru"
        self.assertTrue(self.auth.checkLogin(login))

    def test_phone_login(self):
        login = "+7-123-123-1234"
        self.assertTrue(self.auth.checkLogin(login))

    def test_short_len_login(self):
        login = "af"
        with self.assertRaisesRegex(ValueError,"Логин должен быть из пяти или больше символов"):
            self.auth.checkLogin(login)

    def test_four_len_login(self):
        login = "afed"
        with self.assertRaisesRegex(ValueError,"Логин должен быть из пяти или больше символов"):
            self.auth.checkLogin(login)

    def test_five_len_login(self):
        login = "adfgh"
        self.assertTrue(self.auth.checkLogin(login))

    def test_login_with_cyrillic(self):
        login = "кцпцкппцк"
        with self.assertRaisesRegex(ValueError,"Логин должен содержать только латинские буквы, цифры и нижнее подчеркивание"):
            self.auth.checkLogin(login)

    def test_login_with_spec_symbol(self):
        login = "werfwef@!"
        with self.assertRaisesRegex(ValueError,"Логин должен содержать только латинские буквы, цифры и нижнее подчеркивание"):
            self.auth.checkLogin(login)

    def test_black_list_login(self):
        login = "admin"
        with self.assertRaisesRegex(ValueError,"Этот логин нельзя использовать"):
            self.auth.checkLogin(login)

    def test_black_list_login_with_random_case(self):
        login = "AdmIN"
        with self.assertRaisesRegex(ValueError,"Этот логин нельзя использовать"):
            self.auth.checkLogin(login)

    def test_correct_login(self):
        login = "adfg_hfe1"
        self.assertTrue(self.auth.checkLogin(login))

    def test_six_len_password(self):
        password = "кпуЕ1!"
        with self.assertRaisesRegex(ValueError,"Пароль должен быть из семи или больше символов"):
            self.auth.checkPassword(password, password)

    def test_seven_len_password(self):
        password = "кпуЕ123!"
        self.assertTrue(self.auth.checkPassword(password,password))

    def test_password_with_latin(self):
        password = "кпуЕ123!Q"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать только кириллицу, цифры и спецсимволы"):
            self.auth.checkPassword(password, password)

    def test_password_without_letters(self):
        password = "3124124123!"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать хотя бы одну букву в верхнем регистре"):
            self.auth.checkPassword(password, password)

    def test_password_without_uppercase_letters(self):
        password = "кпкцп24123!"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать хотя бы одну букву в верхнем регистре"):
            self.auth.checkPassword(password, password)

    def test_password_without_lowercase_letters(self):
        password = "КАЦПМКЦП24123!"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать хотя бы одну букву в нижнем регистре"):
            self.auth.checkPassword(password, password)

    def test_password_without_numbers(self):
        password = "уаупупК!"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать хотя бы одну цифру"):
            self.auth.checkPassword(password, password)

    def test_password_without_symbols(self):
        password = "уаупупК1"
        with self.assertRaisesRegex(ValueError, "Пароль должен содержать хотя бы один спецсимвол"):
            self.auth.checkPassword(password, password)

    def test_password_different_check_password(self):
        password = "уаупупК1"
        check_password = "123"
        with self.assertRaisesRegex(ValueError, "Пароли не совпадают"):
            self.auth.checkPassword(password, check_password)

    def test_correct_password(self):
        password = "цкпкцпцкпцкпкцП1!"
        self.assertTrue(self.auth.checkPassword(password, password))

if __name__ == '__main__':
    unittest.main()