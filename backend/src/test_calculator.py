import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    ############    Сложение    #############

    def test_addition_base(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 3), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, -4), -5)
        self.assertEqual(self.calculator.addition(-3, 5), 2)
        self.assertEqual(self.calculator.addition(3, -5), -2)
        self.assertEqual(self.calculator.addition(10, -10), 0)

    def test_addition_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.4, 2.5), 3.9)

    def test_addition_infinity(self):
        self.assertEqual(
            self.calculator.addition(float("inf"), float("inf")), float("inf")
        )
        self.assertEqual(
            self.calculator.addition(float("-inf"), float("-inf")), float("-inf")
        )
        self.assertTrue(
            math.isnan(self.calculator.addition(float("inf"), float("-inf")))
        )

    def test_addition_string(self):
        self.assertEqual(self.calculator.addition("1", "5"), "15")

    def test_addition_array(self):
        self.assertEqual(self.calculator.addition([5, 4], [3, 2]), [5, 4, 3, 2])

    def test_addition_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("string", 3)
        with self.assertRaises(TypeError):
            self.calculator.addition({"1": 2}, 3)
        with self.assertRaises(TypeError):
            self.calculator.addition([1, 2], 3)

    ############    Умножение    #############

    def test_multiplication_base(self):
        self.assertEqual(self.calculator.multiplication(0, 3), 0)
        self.assertEqual(self.calculator.multiplication(2, 5), 10)
        self.assertEqual(self.calculator.multiplication(0, 1), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertEqual(self.calculator.multiplication(-2, -1), 2)
        self.assertEqual(self.calculator.multiplication(3, -2), -6)

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(1.5, 2), 3)
        self.assertEqual(self.calculator.multiplication(0.5, 5), 2.5)
        self.assertEqual(self.calculator.multiplication(0.33, 3), 0.99)

    def test_multiplication_infinity(self):
        self.assertEqual(
            self.calculator.multiplication(float("inf"), float("inf")), float("inf")
        )
        self.assertEqual(
            self.calculator.multiplication(float("-inf"), float("-inf")), float("inf")
        )
        self.assertEqual(
            self.calculator.multiplication(float("-inf"), 1), float("-inf")
        )
        self.assertEqual(self.calculator.multiplication(1, float("inf")), float("inf"))
        self.assertEqual(
            self.calculator.multiplication(float("inf"), -1), float("-inf")
        )
        self.assertEqual(
            self.calculator.multiplication(-1, float("-inf")), float("inf")
        )
        self.assertTrue(math.isnan(self.calculator.multiplication(float("inf"), 0)))
        self.assertTrue(math.isnan(self.calculator.multiplication(0, float("-inf"))))

    def test_multiplication_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication([6, 2], [3, 1])
            self.calculator.multiplication("a", "b")

    ############    Вычитание    #############

    def test_subtract_base(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(3, 4), -1)
        self.assertEqual(self.calculator.subtraction(5, 4), 1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtraction(3, -4), 7)
        self.assertEqual(self.calculator.subtraction(-3, 4), -7)
        self.assertEqual(self.calculator.subtraction(-3, -4), 1)

    def test_subtract_float(self):
        self.assertEqual(self.calculator.subtraction(3.5, 1.5), 2)
        self.assertEqual(self.calculator.subtraction(0.5, 4), -3.5)
        self.assertEqual(self.calculator.subtraction(2.5, 1), 1.5)

    def test_subtract_infinity(self):
        self.assertTrue(
            math.isnan(self.calculator.subtraction(float("-inf"), float("-inf")))
        )
        self.assertTrue(
            math.isnan(self.calculator.subtraction(float("inf"), float("inf")))
        )

    def test_subtract_type_error(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "test", 2)
        self.assertRaises(TypeError, self.calculator.subtraction, "a", "b")
        self.assertRaises(TypeError, self.calculator.subtraction, {}, 3)
        self.assertRaises(TypeError, self.calculator.subtraction, [], 3)

    ############    Деление    #############

    def test_division(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(0, 3), 0)
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(3, 0), None)

    def test_division_negative(self):
        self.assertAlmostEqual(self.calculator.division(-10, 3), -10 / 3)
        self.assertAlmostEqual(self.calculator.division(10, -3), -10 / 3)
        self.assertAlmostEqual(self.calculator.division(-10, -3), 10 / 3)

    def test_division_float(self):
        self.assertEqual(self.calculator.division(6.0, 2.0), 3.0)

    def test_division_infinity(self):
        self.assertEqual(self.calculator.division(float("inf"), 1), float("inf"))
        self.assertEqual(self.calculator.division(float("-inf"), 1), float("-inf"))
        self.assertEqual(self.calculator.division(1, float("inf")), 0)

        self.assertTrue(
            math.isnan(self.calculator.division(float("inf"), float("inf")))
        )
        self.assertTrue(
            math.isnan(self.calculator.division(float("-inf"), float("-inf")))
        )
        self.assertTrue(
            math.isnan(self.calculator.division(float("inf"), float("-inf")))
        )
        self.assertTrue(
            math.isnan(self.calculator.division(float("-inf"), float("inf")))
        )

    def test_division_type_error(self):
        self.assertRaises(TypeError, self.calculator.division, "test", 2)
        self.assertRaises(TypeError, self.calculator.division, "a", "b")
        self.assertRaises(TypeError, self.calculator.division, {}, 3)
        self.assertRaises(TypeError, self.calculator.division, [], 3)

    ############    Модуль     #############

    def test_abs_positive(self):
        self.assertEqual(self.calculator.absolute(3), 3)
        self.assertEqual(self.calculator.absolute(3.5), 3.5)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.absolute(-4), 4)
        self.assertEqual(self.calculator.absolute(-4.5), 4.5)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_type_error(self):
        self.assertRaises(TypeError, self.calculator.absolute, "test", 2)
        self.assertRaises(TypeError, self.calculator.absolute, "a", "b")
        self.assertRaises(TypeError, self.calculator.absolute, {}, 3)
        self.assertRaises(TypeError, self.calculator.absolute, [], 3)

    ############    Возведение в степень     #############

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(1, 100), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_negative(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_float(self):
        self.assertAlmostEqual(self.calculator.degree(2.0, 3.0), 8.0)

    def test_degree_infinity(self):
        self.assertEqual(self.calculator.degree(2, float("inf")), float("inf"))
        self.assertEqual(self.calculator.degree(float("inf"), 2), float("inf"))
        self.assertEqual(self.calculator.degree(float("-inf"), 2), float("inf"))

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_type_error(self):
        self.assertRaises(TypeError, self.calculator.degree, "test", 2)
        self.assertRaises(TypeError, self.calculator.degree, "a", "b")
        self.assertRaises(TypeError, self.calculator.degree, {}, 3)
        self.assertRaises(TypeError, self.calculator.degree, [], 3)

    ############    Логарифм натуральный    #############

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(0.5), math.log(0.5))

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_ln_infinity(self):
        self.assertEqual(self.calculator.ln(float("inf")), float("inf"))

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_float(self):
        self.assertEqual(self.calculator.ln(2.0), 0.6931471805599453)

    def test_ln_type_error(self):
        self.assertRaises(TypeError, self.calculator.ln, "test")
        self.assertRaises(TypeError, self.calculator.ln, "a")
        self.assertRaises(TypeError, self.calculator.ln, {})
        self.assertRaises(TypeError, self.calculator.ln, [])

    ############    Логарифм десятичный    #############

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)
        self.assertAlmostEqual(self.calculator.log(10, 10), 1)
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)
        self.assertAlmostEqual(self.calculator.log(1, 2), 0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-100, 10)

    def test_log_infinity(self):
        self.assertEqual(self.calculator.log(float("inf"), 10), float("inf"))
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_log_type_error(self):
        self.assertRaises(TypeError, self.calculator.log, "test")
        self.assertRaises(TypeError, self.calculator.log, "a")
        self.assertRaises(TypeError, self.calculator.log, {})
        self.assertRaises(TypeError, self.calculator.log, [])

    ############    Корень квадратный    #############

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        result = self.calculator.sqrt(-9)
        self.assertIsInstance(result, complex)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.0), 1.4142135623730951)

    def test_sqrt_infinity(self):
        self.assertEqual(self.calculator.sqrt(float("inf")), float("inf"))
        self.assertFalse(math.isnan(self.calculator.sqrt(float("-inf"))))

    def test_sqrt_type_error(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "test")
        self.assertRaises(TypeError, self.calculator.sqrt, "a")
        self.assertRaises(TypeError, self.calculator.sqrt, {})
        self.assertRaises(TypeError, self.calculator.sqrt, [])

    ############    Корень произвольный    #############
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(0, 5), 0)

    def test_nth_root_negative(self):
        result = self.calculator.nth_root(-8, 3)
        self.assertIsInstance(result, complex)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(8.0, 3.0), 2.0)

    def test_nth_root_infinity(self):
        self.assertEqual(self.calculator.nth_root(float("inf"), 3), float("inf"))

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)

    def test_nth_root_type_error(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "test", 3)
        self.assertRaises(TypeError, self.calculator.nth_root, 3, "a")
        self.assertRaises(TypeError, self.calculator.nth_root, {}, 3)
        self.assertRaises(TypeError, self.calculator.nth_root, [], 3)


if __name__ == "__main__":
    unittest.main()
