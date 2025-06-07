import unittest
import os
from load.load import load_to_csv

class TestLoad(unittest.TestCase):
    def test_load_to_csv_creates_file(self):
        data = {"city": "London", "temperature": 15, "condition": "Cloudy"}
        filepath = "test_output.csv"
        load_to_csv(data, filepath)
        self.assertTrue(os.path.exists(filepath))
        os.remove(filepath)
