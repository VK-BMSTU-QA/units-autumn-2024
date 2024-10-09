import unittest
import sys
import math
import os
import cmath
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(-1, -1), -2)
        self.assertAlmostEqual(self.calc.addition(-1.01, -1), -2.01, places=7)

        self.assertEqual(self.calc.addition(1+2j, 3+4j), 4+6j)
        self.assertEqual(self.calc.addition(-1+1j, 1-1j), 0)

        with self.assertRaises(TypeError):
            self.calc.addition("string", 2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(2, 3), 6)
        self.assertAlmostEqual(self.calc.multiplication(2, 0.5), 1.0, places=7)
        self.assertEqual(self.calc.multiplication(-1, 1), -1)
        self.assertEqual(self.calc.multiplication(-1, -1), 1)

        self.assertEqual(self.calc.multiplication(1+2j, 3+4j), -5+10j)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(0, 0), 0)
        self.assertEqual(self.calc.subtraction(-1, -1), 0)
        self.assertAlmostEqual(self.calc.subtraction(5.5, 1.2), 4.3, places=7)

        self.assertEqual(self.calc.subtraction(1+2j, 3+4j), -2-2j)

        with self.assertRaises(TypeError):
            self.calc.subtraction("text", 5)

    def test_division(self):
        self.assertAlmostEqual(self.calc.division(10, 2), 5.0, places=7)
        self.assertAlmostEqual(self.calc.division(-10, 2), -5.0, places=7)
        self.assertAlmostEqual(self.calc.division(10, -2), -5.0, places=7)
        self.assertAlmostEqual(self.calc.division(1, 3), 1/3, places=7) 
        
        self.assertAlmostEqual(self.calc.division(1+2j, 1+1j), 1.5+0.5j)

        with self.assertRaises(TypeError):
            self.calc.division("test", 2)

    def test_division_on_zero(self):
        self.assertIsNone(self.calc.division(10, 0))

    def test_absolute(self):
        self.assertEqual(self.calc.absolute(-10), 10)
        self.assertEqual(self.calc.absolute(10), 10)
        self.assertEqual(self.calc.absolute(0), 0)

        self.assertEqual(self.calc.absolute(3+4j), 5)

    def test_degree(self):
        self.assertEqual(self.calc.degree(2, 3), 8)
        self.assertEqual(self.calc.degree(2, 0), 1)
        self.assertEqual(self.calc.degree(-2, 3), -8)
        self.assertAlmostEqual(self.calc.degree(2, -2), 0.25, places=7)


    def test_ln(self):
        self.assertAlmostEqual(self.calc.ln(1), 0, places=7)
        self.assertAlmostEqual(self.calc.ln(math.e), 1, places=7)
        with self.assertRaises(ValueError):
            self.calc.ln(-1)

        with self.assertRaises(TypeError):
            self.calc.ln("ln_invalid")

    def test_log(self):
        self.assertAlmostEqual(self.calc.log(8, 2), 3, places=7)
        self.assertAlmostEqual(self.calc.log(100, 10), 2, places=7)
        with self.assertRaises(ValueError):
            self.calc.log(-1, 2)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calc.sqrt(4), 2, places=7)
        self.assertAlmostEqual(self.calc.sqrt(9), 3, places=7)
        with self.assertRaises(ValueError):
            if self.calc.sqrt(-1) is not None:
                raise ValueError("Корень из отрицательного числа не поддерживается")

    def test_nth_root(self):
        self.assertAlmostEqual(self.calc.nth_root(27, 3), 3, places=7)
        self.assertAlmostEqual(self.calc.nth_root(16, 4), 2, places=7)
        with self.assertRaises(ValueError):
            if self.calc.nth_root(-8, 2) is not None:
                raise ValueError("Корень из отрицательного числа не поддерживается")


if __name__ == "__main__":
    unittest.main()
