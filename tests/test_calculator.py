import unittest

from selenium import webdriver

from pages.calculator_page import SimpleCalculatorPage
from selenium.common.exceptions import NoSuchElementException

class CalculatorTest(unittest.TestCase):
    URL = "https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.page = SimpleCalculatorPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_addition(self):
        self.page.enter_first_number("5")
        self.page.enter_second_number("3")
        self.page.select_operation("+")

        result = self.page.get_result()

        self.assertEqual(result, 8)

    def test_subtraction(self):
        self.page.enter_first_number("5")
        self.page.enter_second_number("3")
        self.page.select_operation("-")

        result = self.page.get_result()

        self.assertEqual(result, 2)

    def test_multiplication(self):
        self.page.enter_first_number("5")
        self.page.enter_second_number("3")
        self.page.select_operation("*")

        result = self.page.get_result()

        self.assertEqual(result, 15)

    def test_multiplication_big_numbers(self):
        self.page.enter_first_number("14534")
        self.page.enter_second_number("2349")
        self.page.select_operation("*")

        result = self.page.get_result()

        self.assertEqual(result, 34140366)

    def test_division(self):
        self.page.enter_first_number("6")
        self.page.enter_second_number("3")
        self.page.select_operation("/")

        result = self.page.get_result()

        self.assertEqual(result, 2)

    def test_fractional_division(self):
        self.page.enter_first_number("7")
        self.page.enter_second_number("2")
        self.page.select_operation("/")

        result = self.page.get_result()

        self.assertEqual(result, 3.5)

    def test_zero_division(self):
        self.page.enter_first_number("7")
        self.page.enter_second_number("0")
        self.page.select_operation("/")

        result = self.page.get_result()

        self.assertIsNone(result)

    def test_choose_not_exist_operation(self):
        with self.assertRaises(NoSuchElementException):
            self.page.select_operation("abc")