# https://github.com/elliottscarlett-ufl/lab11-ES-EM.git
# Partner 1: Elliott Scarlett
# Partner 2: Elijah Morgan

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): 
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(-2, 2), -4)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 10), 2.5)
        self.assertEqual(div(-2, 8), -4)

    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
              div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(0), 0.0)


if __name__ == "__main__":
    unittest.main()