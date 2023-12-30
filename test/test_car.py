import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_milage = 100000
        last_service_mileage = 6999
        engine = CapuletEngine(current_milage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_milage = 10000
        last_service_mileage = 8000
        engine = CapuletEngine(current_milage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_milage = 100000
        last_service_mileage = 3999
        engine = WilloughbyEngine(current_milage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_milage = 10000
        last_service_mileage = 8000
        engine = WilloughbyEngine(current_milage, last_service_mileage)
        self.assertFalse(engine.needs_service())



class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())



class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
