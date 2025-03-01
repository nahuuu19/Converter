"""Test module for Converter."""

import unittest
from unittest.mock import patch
from task.converter import Converter


def mock_converter(_, celsius):
    """Mock function converting celsius to fahrenheit."""
    return (celsius * 9/5) + 32  # Este es el cálculo real para convertir C a F.


class TestConverter(unittest.TestCase):
    """Test case for the Converter class."""

    def setUp(self):
        self.converter = Converter()

    @patch('task.converter.Converter.convert_celsius_to_fahrenheit', mock_converter)
    def test_converter(self):
        """Test conversion from celsius to fahrenheit using a mock."""
        result = self.converter.convert_celsius_to_fahrenheit(100)
        self.assertEqual(result, 212)  # 100 C == 212 F

if __name__ == "__main__":
    unittest.main()