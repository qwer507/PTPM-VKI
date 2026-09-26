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

if __name__ == '__main__':
    unittest.main()