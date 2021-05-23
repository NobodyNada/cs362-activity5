import unittest
from leapyear import is_leap_year

class LeapyearTests(unittest.TestCase):
    def test_simple_years(self):
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2020))
        self.assertFalse(is_leap_year(2021))
        self.assertTrue(is_leap_year(4))
        self.assertFalse(is_leap_year(3))

    def test_centuries(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(2000))

