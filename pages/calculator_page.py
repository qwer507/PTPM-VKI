from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SimpleCalculatorPage:
    _INPUT_A = (By.CSS_SELECTOR, 'input[ng-model="a"]')
    _INPUT_B = (By.CSS_SELECTOR, 'input[ng-model="b"]')
    _SELECT_OPERATION = (By.CSS_SELECTOR, 'select[ng-model="operation"]')
    _RESULT_TEXT = (By.CSS_SELECTOR, 'b.result')

    def __init__(self, driver):
        self.driver = driver
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(self._INPUT_A)
        )

    def enter_first_number(self, value):
        field = self.driver.find_element(*self._INPUT_A)
        field.clear()
        field.send_keys(str(value))

    def enter_second_number(self, value):
        field = self.driver.find_element(*self._INPUT_B)
        field.clear()
        field.send_keys(str(value))

    # допустимые значения: +, -, *, /
    def select_operation(self, op):
        select_elem = Select(self.driver.find_element(*self._SELECT_OPERATION))
        select_elem.select_by_value(op)

    def get_result(self):
        element = self.driver.find_element(*self._RESULT_TEXT)
        result = element.text.split()[-1]
        if result == "null":
            return None
        else:
            return float(result)