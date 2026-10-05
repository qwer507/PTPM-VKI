import unittest
from src.Delivery import calculate_delivery_cost

class DeliveryTestBase(unittest.TestCase):
    CORRECT_WEIGHT = 10
    CORRECT_DISTANCE = 1000
    CORRECT_PACKAGE_TYPE = "обычный"
    ERROR = (-1, "0000-00-00")

class TestDeliveryValidation(DeliveryTestBase):
    def test_very_light_package(self):
        weight = 0.000002
        self.assertEqual(calculate_delivery_cost(weight, self.CORRECT_DISTANCE, self.CORRECT_PACKAGE_TYPE), self.ERROR)

    def test_negative_weight(self):
        weight = -12
        self.assertEqual(calculate_delivery_cost(weight, self.CORRECT_DISTANCE, self.CORRECT_PACKAGE_TYPE), self.ERROR)

    def test_very_heavy_package(self):
        weight = 99999999
        self.assertEqual(calculate_delivery_cost(weight, self.CORRECT_DISTANCE, self.CORRECT_PACKAGE_TYPE), self.ERROR)

    def test_zero_distance(self):
        dist = 0
        self.assertEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, dist, self.CORRECT_PACKAGE_TYPE), self.ERROR)

    def test_very_big_distance(self):
        dist = 9999999999
        self.assertEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, dist, self.CORRECT_PACKAGE_TYPE), self.ERROR)

    def test_unknow_type_package(self):
        type = "efqfqfqefeqfqe"
        self.assertEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, self.CORRECT_DISTANCE, type), self.ERROR)

    def test_random_case_type_package(self):
        type = "ОбычНый"
        self.assertNotEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, self.CORRECT_DISTANCE, type), self.ERROR)

class TestDeliveryCalcDate(DeliveryTestBase):
    def test_date_with_small_distance_express(self):
        dist = 300
        is_express = True
        self.assertEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, dist, self.CORRECT_PACKAGE_TYPE, is_express)[1], "2026-09-04")

    def test_calc_date(self):
        dist = 2100
        is_express = True
        self.assertEqual(calculate_delivery_cost(self.CORRECT_WEIGHT, dist, self.CORRECT_PACKAGE_TYPE)[1],"2026-09-07")


class TestDeliveryCalcCost(DeliveryTestBase):
    def test_calc_cost(self):
        weight = 3
        dist = 100
        type = "обычный"
        cost = 200 + dist * 5
        self.assertEqual(calculate_delivery_cost(weight, dist, type)[0],cost)

    def test_calc_cost_with_heavy_wight(self):
        weight = 30
        dist = 100
        type = "обычный"
        cost = (200 + dist * 5) * 1.5
        self.assertEqual(calculate_delivery_cost(weight, dist, type)[0],cost)

    def test_calc_cost_with_danger_type(self):
        weight = 3
        dist = 100
        type = "опасный"
        cost = 200 + dist * 5 + 1000
        self.assertEqual(calculate_delivery_cost(weight, dist, type)[0],cost)

    def test_calc_cost_express_delivery(self):
        weight = 3
        dist = 100
        type = "обычный"
        cost = (200 + dist * 5) * 1.5
        self.assertEqual(calculate_delivery_cost(weight, dist, type, True)[0],cost)

if __name__ == '__main__':
    unittest.main()