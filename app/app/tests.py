"""
Sample Tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test Adding numbers."""
        res = calc.add(6, 7)

        self.assertEqual(res, 13)

    def test_subtract_numbers(self):
        """Test Subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, -5)
