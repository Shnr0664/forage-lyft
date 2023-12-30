import unittest

from engine.willoughby_engine import WilloughbyEngine


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
