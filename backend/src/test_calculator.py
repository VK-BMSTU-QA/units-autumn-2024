import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Test addition
    def test_add_positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_mixed(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_float(self):
        self.assertEqual(self.calculator.addition(0.5, 0.5), 1)

    def test_add_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(None, None)
            self.calculator.addition([], 0)

    # Test multiplications
    def test_multiply_positive(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_multiply_mixed(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiplication(5, 0), 0)

    def test_multiply_float(self):
        self.assertEqual(self.calculator.multiplication(0.5, 0.5), 0.25)

    def test_multiply_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, None)
            self.calculator.multiplication([], 0)

    # Test subtraction
    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtraction(-5, -3), -2)

    def test_subtract_mixed(self):
        self.assertEqual(self.calculator.subtraction(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtract_float(self):
        self.assertEqual(self.calculator.subtraction(0.5, 0.25), 0.25)

    def test_subtract_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, None)
            self.calculator.subtraction([], 0)

    # Test division
    def test_divide_positive(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    def test_divide_negative(self):
        self.assertEqual(self.calculator.division(-6, -2), 3)

    def test_divide_mixed(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))

    def test_division_float(self):
        self.assertEqual(self.calculator.division(0.5, 0.25), 2)

    def test_divide_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.division(None, None)
            self.calculator.division(None, [])

    # Test absolute
    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(-0.25), 0.25)

    def test_absolute_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute(None)
            self.calculator.absolute([])

    # Test degree
    def test_degree_positive_base_positive_power(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_positive_base_negative_power(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_negative_base_even_power(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree_negative_base_odd_power(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_zero_base_nonzero_power(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    def test_degree_nonzero_base_zero_power(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree_float_base(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_float(self):
        self.assertEqual(self.calculator.degree(0.5, 3), 0.125)

    def test_degree_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(None, None)
            self.calculator.degree(None, [])

    # Test ln
    def test_ln_positive(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_one(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln_less_than_one(self):
        self.assertLess(self.calculator.ln(0.5), 0)

    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(0.5), -0.693147181)

    def test_ln_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.ln(None)
            self.calculator.ln([])

    # Test log
    def test_log_positive_base_and_number(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_one_as_base(self):
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)

    def test_log_float_base(self):
        self.assertAlmostEqual(self.calculator.log(0.25, 0.5), 2)

    def test_log_one_as_number(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(10, 1)

    def test_log_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0.5, 10)
            self.calculator.log(100, 0)

    def test_log_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.log(None, None)
            self.calculator.log(None, [])

    # Test sqrt
    def test_sqrt_positive(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(0.25), 0.5)

    def test_sqrt_negative(self):
        result = self.calculator.sqrt(-1)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result.real, 0)
        self.assertAlmostEqual(result.imag, 1)

    def test_sqrt_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)
            self.calculator.sqrt([])

    # Tests nth root
    def test_nth_root_positive(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)

    def test_nth_root_float(self):
        self.assertEqual(self.calculator.nth_root(0.125, 3), 0.5)

    def test_nth_root_negative_complex_result(self):
        result = self.calculator.nth_root(-1, 2)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result.real, 0)
        self.assertAlmostEqual(result.imag, 1)

    def test_nth_root_non_integer_power(self):
        self.assertAlmostEqual(self.calculator.nth_root(16, 0.5), 256)

    def test_nth_root_wrong_types(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, None)
            self.calculator.nth_root(None, [])


if __name__ == "__main__":
    unittest.main()
