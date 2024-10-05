import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.9), 4.0)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-2, 2), 0)

    def test_addition_strings(self):
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')

    def test_addition_lists(self):
        self.assertEqual(self.calculator.addition([1, 2], [3]), [1, 2, 3])

    def test_addition_infinity(self):
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)

    def test_addition_type_error(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, 'string')

    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multiplication_negative_int(self):
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)

    def test_multiplication_strings(self):
        self.assertEqual(self.calculator.multiplication(3, 's'), 'sss')

    def test_multiplication_lists(self):
        self.assertEqual(self.calculator.multiplication(3, [0]), [0, 0, 0])

    def test_multiplication_infinity(self):
        self.assertEqual(self.calculator.multiplication(2, math.inf), math.inf)

    def test_multiplication_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.1, 2.5), 2.75)

    def test_multiplication_type_error(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'string')

    def test_subtraction_zero(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(2, -2), 4)

    def test_subtraction_negative_values(self):
        self.assertEqual(self.calculator.subtraction(-2, -2), 0)

    def test_subtraction_infinity(self):
        self.assertEqual(self.calculator.subtraction(-2, math.inf), -math.inf)

    def test_subtraction_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.1, 2.1), 0.0)

    def test_subtraction_float_negative(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.1, -2.1), 4.2)

    def test_subtraction_type_error(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'string')

    def test_division_int(self):
        self.assertEqual(self.calculator.division(8, 2), 4)

    def test_division_negative_int(self):
        self.assertEqual(self.calculator.division(-8, 2), -4)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(-8, -2), 4)

    def test_division_infinity(self):
        self.assertEqual(self.calculator.division(math.inf, 5), math.inf)

    def test_division_float_negative(self):
        self.assertAlmostEqual(self.calculator.division(-8, math.inf), 0)

    def test_division_float(self):
        self.assertAlmostEqual(self.calculator.division(8.4, 4.2), 2.0)

    def test_division_float_precision(self):
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.3333, places=4)

    def test_division_zero(self):
        self.assertIsNone(self.calculator.division(8, 0))

    def test_division_type_error(self):
        self.assertRaises(TypeError, self.calculator.division, 1, 'string')

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_negative_infinity(self):
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    def test_absolute_float(self):
        self.assertAlmostEqual(self.calculator.absolute(-5.1), 5.1)

    def test_absolute_type_error(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'string')

    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_zero_exponent(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_negative_base(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_float_exponent(self):
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_float_base_exponent(self):
        self.assertAlmostEqual(self.calculator.degree(2, 1.1), 2.14355, places=5)

    def test_degree_float_base(self):
        self.assertAlmostEqual(self.calculator.degree(1.1, 1.1), 1.11053, places=5)

    def test_degree_type_error_1(self):
        self.assertRaises(TypeError, self.calculator.degree, 1, 'string')

    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_e(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_infinity(self):
        self.assertAlmostEqual(self.calculator.ln(math.inf), math.inf)

    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(2.71), 0.9969, places=4)

    def test_ln_type_error(self):
        self.assertRaises(TypeError, self.calculator.ln, 'string')

    def test_ln_value_error(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_log_base_10(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_base_float(self):
        self.assertAlmostEqual(self.calculator.log(1.1, 2.2), 0.1209, places=4)

    def test_log_infinity_base_10(self):
        self.assertAlmostEqual(self.calculator.log(100, math.inf), 0)

    def test_log_infinity_base_2(self):
        self.assertAlmostEqual(self.calculator.log(math.inf, 2), math.inf)

    def test_log_value_error_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -1, 10)

    def test_log_value_error_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)

    def test_log_type_error(self):
        self.assertRaises(TypeError, self.calculator.log, 1, 'string')

    def test_sqrt_int(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(9.1), 3.0166, places=4)

    def test_sqrt_large_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(10), 3.16227, places=4)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_infinity(self):
        self.assertAlmostEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_negative_infinity(self):
        self.assertAlmostEqual(self.calculator.sqrt(-math.inf), math.inf)

    def test_sqrt_complex_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), complex(6.123233995736766e-17, 1))

    def test_sqrt_type_error_string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'string')

    def test_sqrt_type_error_list(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])

    def test_nth_root_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(8.1, 3.2), 1.92265, places=4)

    def test_nth_root_negative_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(-8.1, 3.2), complex(1.0681703947507033, 1.5986299682925724))

    def test_nth_root_infinity(self):
        self.assertAlmostEqual(self.calculator.nth_root(math.inf, 3), math.inf)

    def test_nth_root_infinity_infinity(self):
        self.assertAlmostEqual(self.calculator.nth_root(math.inf, math.inf), 1)

    def test_nth_root_negative_infinity_infinity(self):
        self.assertAlmostEqual(self.calculator.nth_root(-math.inf, math.inf), 1)

    def test_nth_root_negative_infinity_negative_infinity(self):
        self.assertAlmostEqual(self.calculator.nth_root(-math.inf, -math.inf), 1)

    def test_nth_root_type_error(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 1, 'string')

    def test_nth_root_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)



if __name__ == "__main__":
    unittest.main()
