import unittest
from unittest.mock import patch

from src.WorkWithUser import WorkWithUser

class TestWorkWithUserGetData(unittest.TestCase):

    def setUp(self):
        self.user = WorkWithUser()

    def test_returns_tuple_of_three(self):
        with patch("builtins.input", side_effect=["alice", "secret", "secret"]):
            result = self.user.getData()

        self.assertEqual(result, ("alice", "secret", "secret"))

    def test_returns_empty(self):
        with patch("builtins.input", side_effect=["", "", ""]):
            result = self.user.getData()

        self.assertEqual(result, ("", "", ""))


if __name__ == "__main__":
    unittest.main()