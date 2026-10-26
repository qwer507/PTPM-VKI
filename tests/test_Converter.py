import unittest
from src.Converter import Converter

class TestConverter(unittest.TestCase):
    def test_big_x(self):
        x = 9999999999.1

        result = Converter.do(x)

        self.assertEqual(result, 1000)

    def test_x_is_100_7(self):
        x = 100.7

        result = Converter.do(x)

        self.assertEqual(result, 1000)

    def test_x_greater_0_less_100_7(self):
        x = 50.2

        result = Converter.do(x)

        self.assertEqual(result, 50)

    def test_x_is_0(self):
        x = 0

        with self.assertRaisesRegex(ValueError, "X не может быть 0"):
            result = Converter.do(x)

    def test_x_less_0_greater_minus_30_4(self):
        x = -12.3

        result = Converter.do(x)

        self.assertEqual(result, -17)

    def test_x_is_minus_30_4(self):
        x = -30.4

        result = Converter.do(x)

        self.assertEqual(result, -35)

    def test_x_less_minus_30_4(self):
        x = -9999999

        result = Converter.do(x)

        self.assertEqual(result, -2000)