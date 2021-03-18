import unittest
import Calculation

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calculation.add(5,6)
        self.assertEqual(11, result)

    def test_substract(self):
        result = Calculation.subtract(16,8)
        self.assertEqual(8, result)

    def test_divide(self):
        result = Calculation.divide(16, 2)
        self.assertTrue(8, result)

    def test_multiply(self):
        result = Calculation.multiply(8, 2)
        self.assertEqual(16, result)

if __name__ == '__main__':
        unittest.main()