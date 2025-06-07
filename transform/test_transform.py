import unittest
from transform.transform import transform_weather_data

class TestTransform(unittest.TestCase):
    def test_transform_weather_data(self):
        input_data = {
            "location": {"name": "London"},
            "current": {"temp_c": 15, "condition": {"text": "Cloudy"}}
        }
        result = transform_weather_data(input_data)
        self.assertEqual(result["city"], "London")
        self.assertEqual(result["temperature"], 15)
        self.assertEqual(result["condition"], "Cloudy")
