import unittest

from src.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(db_path=":memory:")

    def tearDown(self):
        self.db.con.close()

    def test_find_by_id(self):
        data = (1,"abc","eqeqweqweqw")
        self.db.add(data[0],data[1],data[2])

        result = self.db.get_by_id(1)

        self.assertEqual(result,data)

    def test_find_nonexistent_by_id(self):
        result = self.db.get_by_id(12)

        self.assertIsNone(result)

    def test_find_by_name(self):
        data_1 = (1,"abc","eqeqweqweqw")
        data_2 = (2, "qwefq", "afsfsa")
        data_3 = (3,"abc","123123123123")
        self.db.add(data_1[0], data_1[1], data_1[2])
        self.db.add(data_2[0], data_2[1], data_2[2])
        self.db.add(data_3[0], data_3[1], data_3[2])

        result = self.db.get_by_name("abc")

        self.assertEqual(result, [data_1,data_3])

    def test_find_nonexistent_by_name(self):
        result = self.db.get_by_name("afdsfa")

        self.assertEqual(result,[])

    def test_add(self):
        data = (2, "qwefq", "afsfsa")

        result = self.db.add(data[0],data[1],data[2])

        self.assertTrue(result)
        self.assertEqual(data, self.db.get_by_id(data[0]))

    def test_add_with_same_id(self):
        data_1 = (2, "qwefq", "afsfsa")
        data_2 = (2, "qweqweqwe", "123123123")

        result_1 = self.db.add(data_1[0],data_1[1],data_1[2])
        result_2 = self.db.add(data_2[0], data_2[1], data_2[2])

        self.assertTrue(result_1)
        self.assertFalse(result_2)

    def test_update(self):
        data = (2, "qwe", "1324124124")
        new_message = "efwefewfeqf"
        self.db.add(data[0],data[1],data[2])

        result = self.db.update(data[0],new_message)

        self.assertTrue(result)
        self.assertEqual(new_message, self.db.get_by_id(data[0])[2])

    def test_update_nonexist_data(self):
        result = self.db.update(12,"qweqwe")

        self.assertEqual(self.db.cursor.rowcount, 0)