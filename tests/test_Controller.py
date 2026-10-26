import unittest
from unittest.mock import patch, MagicMock

from src.CheckLoginData import Authorization
from src.WorkWithDB import WorkWithDB
from src.WorkWithUser import WorkWithUser
from src.Controller import Controller

class TestControllerIntegration(unittest.TestCase):

    def setUp(self):
        self.db = WorkWithDB(db_path=":memory:")
        self.auth = Authorization()
        self.user = WorkWithUser()
        self.email = MagicMock()

        self.controller = Controller(
            auth=self.auth,
            db=self.db,
            user=self.user,
            email=self.email,
        )

    def tearDown(self):
        self.db.con.close()

    def _start_with_input(self, login, password, check):
        with patch("builtins.input", side_effect=[login, password, check]):
            return self.controller.start()

    def _count_rows(self):
        cur = self.db.con.cursor()
        cur.execute("SELECT COUNT(*) FROM AuthLog")
        return cur.fetchone()[0]

    def test_success_data(self):
        result = self._start_with_input("newuser", "Пароль1!", "Пароль1!")

        self.assertTrue(result[3])

        stored = self.db.find("newuser", "Пароль1!", "Пароль1!")
        self.assertEqual(stored, ("newuser", "Пароль1!", "Пароль1!", 1, ""))

    def test_not_success_data(self):
        result = self._start_with_input("abc", "Пароль1!", "Пароль1!")

        self.assertFalse(result[3])

        stored = self.db.find("abc", "Пароль1!", "Пароль1!")
        self.assertIsNotNone(stored)
        self.assertEqual(stored[3], 0)

    def test_second_identical_attempt_uses_cached_record(self):
        first = self._start_with_input("newuser", "Пароль1!", "Пароль1!")
        rows_after_first = self._count_rows()

        second = self._start_with_input("newuser", "Пароль1!", "Пароль1!")

        self.assertEqual(self._count_rows(), rows_after_first)

    def test_different_logins_produce_separate_rows(self):
        self._start_with_input("user1", "Пароль1!", "Пароль1!")
        self._start_with_input("user2", "Пароль1!", "Пароль1!")

        self.assertIsNotNone(self.db.find("user1", "Пароль1!", "Пароль1!"))
        self.assertIsNotNone(self.db.find("user2", "Пароль1!", "Пароль1!"))

if __name__ == "__main__":
    unittest.main()