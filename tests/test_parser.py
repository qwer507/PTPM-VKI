import unittest
from pathlib import Path
from src.parser import ForumParser

class TestDatabase(unittest.TestCase):
    TEST_FILE = Path(__file__).resolve().parent / "test.html"

    def setUp(self):
        self.parser = ForumParser()

    def tearDown(self):
        self.parser = None

    def test_find_ids(self):
        file = self.TEST_FILE
        need_id = [122900110,122928321,123166495,129522274,129523254,143300612]

        data = self.parser.parse_page(file, from_file=True)

        for index, post in enumerate(data):
            self.assertEqual(post[0], need_id[index])

    def test_find_names(self):
        file = self.TEST_FILE
        need_id = ["uilavashou","Ivan 2011","Forpdaforpda","S1MASHFM","tranzit-48","Lenny_345"]

        data = self.parser.parse_page(file, from_file=True)

        for index, post in enumerate(data):
            self.assertEqual(post[1], need_id[index])