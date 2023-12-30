import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_needs_service(self):
        wear = [0.5, 0.8, 0.9, 0.92]
        tire = OctoprimeTire(wear)
        self.assertTrue(tire.needs_service())

    def test_tire_does_not_need_service(self):
        wear = [0.5, 0.5, 0.5, 0.3]
        tire = CarriganTire(wear)
        self.assertFalse(tire.needs_service())
