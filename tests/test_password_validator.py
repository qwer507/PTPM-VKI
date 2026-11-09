import unittest

from src.password_validator import PasswordValidator


class TestPasswordValidator(unittest.TestCase):
    def setUp(self):
        self.valid = PasswordValidator()

    def tearDown(self):
        self.valid = None

    def test_cyrillic_password(self):
        password = "ацацуаАК123@"
        result = self.valid.validator_password(password)
        self.assertTrue(result)

    def test_latin_password(self):
        password = "adfadsDF123@"
        result = self.valid.validator_password(password)
        self.assertTrue(result)

    def test_len_7_password(self):
        password = "adDF1@2"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_len_8_password(self):
        password = "1adDF1@2"
        result = self.valid.validator_password(password)
        self.assertTrue(result)

    def test_len_20_password(self):
        password = "adDF1@2aaaaaaaaaaaaa"
        result = self.valid.validator_password(password)
        self.assertTrue(result)

    def test_len_21_password(self):
        password = "adDF1@2aaaaaaaaaaaaaa"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_password_without_upper(self):
        password = "abcabcabc1@"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_password_without_lower(self):
        password = "ABCABCABC1@"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_password_without_digit(self):
        password = "abcabcabcA@"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_password_without_spec(self):
        password = "abcabcabcA1"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_password_without_need_spec(self):
        password = "abcabcabcA1_"
        result = self.valid.validator_password(password)
        self.assertFalse(result)

    def test_not_str_password(self):
        password = 12
        with self.assertRaises(TypeError):
            result = self.valid.validator_password(password)

    def test_password_with_space(self):
        password = "asdaf asfasf"
        with self.assertRaises(ValueError):
            result = self.valid.validator_password(password)