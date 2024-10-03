import unittest
import sys
import os
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(3, 2), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(-1, -1), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(3, 2), 6)
        self.assertEqual(self.calc.multiplication(-1, 1), -1)
        self.assertEqual(self.calc.multiplication(0, 100), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(3, 2), 1)
        self.assertEqual(self.calc.subtraction(2, 3), -1)
        self.assertEqual(self.calc.subtraction(-1, -1), 0)

    def test_division(self):
        self.assertEqual(self.calc.division(6, 3), 2)
        self.assertEqual(self.calc.division(5, 2), 2.5)
        self.assertIsNone(self.calc.division(5, 0))  # Негативный кейс

    def test_absolute(self):
        self.assertEqual(self.calc.absolute(-5), 5)
        self.assertEqual(self.calc.absolute(5), 5)

    def test_degree(self):
        self.assertEqual(self.calc.degree(2, 3), 8)
        self.assertEqual(self.calc.degree(5, 0), 1)

    def test_ln(self):
        self.assertAlmostEqual(self.calc.ln(math.e), 1)
        with self.assertRaises(ValueError):
            self.calc.ln(-1)  # негативный кейс
        with self.assertRaises(ValueError):
            self.calc.ln(0)

    def test_log(self):
        self.assertEqual(self.calc.log(8, 2), 3)
        with self.assertRaises(ValueError):
            self.calc.log(-1, 2)  # негативный кейс

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)

    def test_nth_root(self):
        self.assertEqual(self.calc.nth_root(8, 3), 2)
        self.assertEqual(self.calc.nth_root(27, 3), 3)


if __name__ == "__main__":
    unittest.main()
