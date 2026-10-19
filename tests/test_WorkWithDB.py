import sqlite3
import unittest

from src.WorkWithDB import WorkWithDB

class TestWorkWithDB(unittest.TestCase):

    def setUp(self):
        self.db = WorkWithDB(db_path=":memory:")

    def tearDown(self):
        self.db.con.close()

    def test_add_and_find(self):
        self.db.add("user1", "pass1", "pass1", True, None)
        result = self.db.find("user1", "pass1", "pass1")
        self.assertEqual(result, ("user1", "pass1", "pass1", 1, None))

    def test_find_nonexistent(self):
        self.assertIsNone(self.db.find("no_user", "no_pass", "no_pass"))

    def test_add_with_error(self):
        self.db.add("user2", "pass2", "pass2", False, "Пароли не совпадают")
        result = self.db.find("user2", "pass2", "pass2")
        self.assertEqual(
            result, ("user2", "pass2", "pass2", 0, "Пароли не совпадают")
        )

    def test_delete(self):
        self.db.add("user3", "pass3", "pass3", True, None)
        self.assertIsNotNone(self.db.find("user3", "pass3", "pass3"))

        self.db.delete("user3", "pass3", "pass3")
        self.assertIsNone(self.db.find("user3", "pass3", "pass3"))

    def test_delete_only_matching(self):
        self.db.add("user4", "pass4", "pass4", True, None)
        self.db.add("user4", "pass4", "other", True, None)

        self.db.delete("user4", "pass4", "pass4")

        self.assertIsNone(self.db.find("user4", "pass4", "pass4"))
        self.assertIsNotNone(self.db.find("user4", "pass4", "other"))

    def test_duplicate_primary_key_raises(self):
        self.db.add("dup", "dup", "dup", True, None)
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add("dup", "dup", "dup", False, "some error")

    def test_find_with_wrong_fields_returns_none(self):
        self.db.add("user5", "correct", "correct", True, None)

        self.assertIsNone(self.db.find("user5", "wrong", "correct"))
        self.assertIsNone(self.db.find("user5", "correct", "wrong"))
        self.assertIsNone(self.db.find("wrong", "correct", "correct"))


if __name__ == "__main__":
    unittest.main()