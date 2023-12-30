import datetime
import unittest

from car_factory import CarFactory


class TestCarFactory(unittest.TestCase):
    def test_calliope_needs_service(self):
        current_date = datetime.date.fromisoformat("2023-12-30")
        last_service_date = datetime.date.fromisoformat("2020-11-25")
        current_milage = 100000
        last_service_milage = 80000
        tire_wear = [0.1, 0.3, 0.5, 0.7]
        car = CarFactory.create_calliope(current_date, last_service_date, current_milage, last_service_milage,
                                         tire_wear)
        self.assertTrue(car.needs_service())
