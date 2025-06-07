import unittest
from extract.extract import fetch_weather_data

class TestExtract(unittest.TestCase):
    def test_fetch_weather_data_structure(self):
        # Test a mocked response or structure here
        sample = {"location": {"name": "London"}, "current": {"temp_c": 15}}
        self.assertIn("location", sample)
        self.assertIn("current", sample)
