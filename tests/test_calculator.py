import unittest

from selenium import webdriver

from pages.calculator_page import SimpleCalculatorPage

class CalculatorTest(unittest.TestCase):
    URL = "https://www.globalsqa.com/angularJs-protractor/SimpleCalculator/"

    def setUp(self):
        self.driver = webdriver.Firefox()
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

        self.assertEqual(result, "8")