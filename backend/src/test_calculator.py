import unittest
import math
from src.calculator import Calculator


class TestCalculatorAdd(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_two_positive_numbers(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_with_negative_number(self):
        self.assertEqual(self.calculator.addition(1, -2), -1)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("abc", 1)


class TestCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_two_positive_numbers(self):
        self.assertEqual(self.calculator.multiplication(4, 5), 20)

    def test_with_negative_number(self):
        self.assertEqual(self.calculator.multiplication(-4, 5), -20)

    def test_with_zero(self):
        self.assertEqual(self.calculator.multiplication(4, 0), 0)

    def test_string(self):
        self.assertEqual(self.calculator.multiplication("ab", 3), "ababab")
        self.assertEqual(self.calculator.multiplication(3, "ab"), "ababab")

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication("ab", "ba")


class TestCalculatorSubstraction(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_two_positive_numbers(self):
        self.assertEqual(self.calculator.subtraction(10, 6), 4)
        self.assertEqual(self.calculator.subtraction(6, 10), -4)

    def test_with_negative_number(self):
        self.assertEqual(self.calculator.subtraction(10, -6), 16)
        self.assertEqual(self.calculator.subtraction(-6, 10), -16)
        self.assertEqual(self.calculator.subtraction(-6, -10), 4)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("abc", 1)


class TestCalculatorDivision(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_two_positive_numbers(self):
        self.assertEqual(self.calculator.division(10, 2), 5.)
        self.assertEqual(self.calculator.division(10, 4), 2.5)

    def test_with_negative_number(self):
        self.assertEqual(self.calculator.division(-10, 5), -2.)
        self.assertEqual(self.calculator.division(10, -5), -2.)
        self.assertEqual(self.calculator.division(-10, -5), 2.)

    def test_with_zero(self):
        self.assertEqual(self.calculator.division(0, -5), 0)

    def test_zero_division(self):
        self.assertIsNone(self.calculator.division(10, 0))

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.division("abc", 1)


class TestCalculatorAbsolute(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_number(self):
        self.assertEqual(self.calculator.absolute(100), 100)

    def test_negative_number(self):
        self.assertEqual(self.calculator.absolute(-100), 100)

    def test_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute("abc")


class TestCalculatorDegree(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)

    def test_negative_degree(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_zero_degree(self):
        self.assertEqual(self.calculator.degree(252, 0), 1)

    def test_one(self):
        self.assertEqual(self.calculator.degree(1, 1000), 1)

    def test_negative_number(self):
        self.assertEqual(self.calculator.degree(-4, 2), 16)
        self.assertEqual(self.calculator.degree(-4, 3), -64)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("abc", 1)


class TestCalculatorLn(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_degree(self):
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)

    def test_negative_degree(self):
        self.assertEqual(self.calculator.ln(math.e ** -2), -2)

    def test_one(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.ln("abc")
        with self.assertRaises(ValueError):
            self.calculator.ln(-100)


class TestCalculatorLog(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_degree(self):
        self.assertEqual(self.calculator.log(4, 2), 2)

    def test_negative_degree(self):
        self.assertEqual(self.calculator.log(0.25, 2), -2)

    def test_one(self):
        self.assertEqual(self.calculator.log(1, 1000), 0)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.log("abc", 10)
        with self.assertRaises(ValueError):
            self.calculator.log(-100, 100)


class TestCalculatorSqrt(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_number(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_one(self):
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_negative_number(self):
        self.assertEqual(type(self.calculator.sqrt(-4)), complex)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt("abc", 1)


class TestCalculatorNthRoot(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_positive_number(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertEqual(self.calculator.nth_root(4, 1), 4)

    def test_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 100), 0)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.calculator.nth_root(0, -100), 0)

    def test_one(self):
        self.assertEqual(self.calculator.nth_root(1, 100), 1)
        self.assertEqual(self.calculator.nth_root(1, -100), 1)

    def test_negative_number(self):
        self.assertEqual(type(self.calculator.nth_root(-4, 2)), complex)
        self.assertEqual(type(self.calculator.nth_root(-4, -2)), complex)
        self.assertEqual(self.calculator.nth_root(-4, 1), -4)

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root("abc", 1)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.calculator.nth_root(4, 0), 1)


if __name__ == "__main__":
    unittest.main()
