import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-2, 2), 0)

    def test_multi(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 3), 0)
        self.assertEqual(self.calculator.subtraction(6, 1), 5)
        self.assertEqual(self.calculator.subtraction(0, 3), -3)

    def test_div(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.division(12, 4), 3)
        self.assertEqual(self.calculator.division(12, -4), -3)
        self.assertEqual(self.calculator.division(12, 0), None)

    def test_abs(self):
        self.assertEqual(self.calculator.absolute(3), 3)
        self.assertEqual(self.calculator.absolute(-3), 3)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)
        self.assertEqual(self.calculator.degree(3, 0), 1)
        self.assertEqual(self.calculator.degree(-3, 2), 9)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_log(self):
        self.assertEqual(self.calculator.log(27, 3), 3)
        self.assertEqual(self.calculator.log(128, 2), 7)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.sqrt(100), 10)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(128, 7), 2)


if __name__ == "main":
    unittest.main()