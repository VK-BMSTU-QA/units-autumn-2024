import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(5, -2), 3)
        self.assertEqual(self.calculator.addition(-1, -4), -5)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(1.2, 3.4), 4.6)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(7, 8), 56)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, -7), 0)
        self.assertEqual(self.calculator.multiplication(70, 0), 0)
        self.assertEqual(self.calculator.multiplication(-3, -5), 15)
        self.assertEqual(self.calculator.multiplication(-3, 5), -15)
        self.assertEqual(self.calculator.multiplication(-0.5, -1.6), 0.8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(7, 4), 3)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(-6, 4), -10)
        self.assertEqual(self.calculator.subtraction(5, -5), 10)
        self.assertEqual(self.calculator.subtraction(-2, -3), 1)
        self.assertEqual(self.calculator.subtraction(-2.4, -3.8), 1.4)

    def test_division(self):
        self.assertEqual(self.calculator.division(56, 8), 7)
        self.assertEqual(self.calculator.division(-32, 16), -2)
        self.assertEqual(self.calculator.division(-14, -7), 2)
        self.assertEqual(self.calculator.division(0.75, -0.25), -3)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(2), 2)
        self.assertEqual(self.calculator.absolute(-2), 2)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-0.38), 0.38)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 4), 81)
        self.assertEqual(self.calculator.degree(0, 100), 0)
        self.assertEqual(self.calculator.degree(100, 0), 1)
        self.assertEqual(self.calculator.degree(1, 100), 1)
        self.assertEqual(self.calculator.degree(-4, 3), -64)
        self.assertAlmostEqual(self.calculator.degree(2, -3), 1/8)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(3.8), 1.33500106673234)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(math.e ** 3), 3)
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(1024, 2), 10)
        self.assertAlmostEqual(self.calculator.log(64, 4), 3)
        self.assertAlmostEqual(self.calculator.log(123, 123), 1)
        self.assertAlmostEqual(self.calculator.log(1, 100), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(64), 8)
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(-100), 10j)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(64, 3), 4)
        self.assertAlmostEqual(self.calculator.nth_root(0, 100), 0)
        self.assertAlmostEqual(self.calculator.nth_root(2, 0.25), 16)
        self.assertAlmostEqual(self.calculator.nth_root(-100, 2), 10j)

    def test_division_negative(self):
        self.assertIsNone(self.calculator.division(1, 0))

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-math.e)

    def test_log_negative(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(100, 1)
        with self.assertRaises(ValueError):
            self.calculator.log(100, -10)
        with self.assertRaises(ValueError):
            self.calculator.log(100, 0)
        with self.assertRaises(ValueError):
            self.calculator.log(-100, 10)

    def test_nth_root_negative(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(100, 0)

    def test_addition_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.addition('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.addition([1, 2], 3)

    def test_multiplication_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication({}, 1)

    def test_subtraction_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], 5)

    def test_division_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.division('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], 5)

    def test_absolute_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute('aaa')
        with self.assertRaises(TypeError):
            self.calculator.absolute([1, 2])

    def test_degree_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], 5)

    def test_ln_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('aaa')
        with self.assertRaises(TypeError):
            self.calculator.ln([1, 2])

    def test_log_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.log('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], 5)

    def test_sqrt_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('aaa')
        with self.assertRaises(TypeError):
            self.calculator.sqrt([1, 2])

    def test_nth_root_wrong_type(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('aaa', 1)
        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], 5)

    def test_addition_unusual_type(self):
        self.assertEqual(self.calculator.addition('aaa', 'bbb'), 'aaabbb')
        self.assertEqual(self.calculator.addition([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_multiplication_unusual_type(self):
        self.assertEqual(self.calculator.multiplication('aaa', 2), 'aaaaaa')
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])

    def test_subtraction_unusual_type(self):
        self.assertEqual(self.calculator.subtraction({1, 2}, {2}), {1})


if __name__ == "__main__":
    unittest.main()
