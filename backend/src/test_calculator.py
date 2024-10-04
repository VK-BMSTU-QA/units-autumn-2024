import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Next 7 tests check positive cases of addition function
    def test_add_positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_positive_1(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_positive_2(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_positive_3(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_add_positive_4(self):
        self.assertTrue(math.isnan(self.calculator.addition(math.inf, -math.inf)))

    def test_add_positive_5(self):
        self.assertEqual(self.calculator.addition(-math.inf, -math.inf), -math.inf)

    def test_add_positive_6(self):
        self.assertEqual(self.calculator.addition(1.222, 3.555), 4.777)

    # Next 6 tests check negative cases of addition function
    def test_add_negative(self):
        self.assertRaises(TypeError, self.calculator.addition, [2, 3], 'asdas')

    def test_add_negative_1(self):
        self.assertRaises(TypeError, self.calculator.addition, 0, 'asdas')

    def test_add_negative_2(self):
        self.assertRaises(TypeError, self.calculator.addition, [2, 3], '34, 43243, 4')

    def test_add_negative_3(self):
        self.assertRaises(TypeError, self.calculator.addition, [2, 3], 0.8)

    def test_add_negative_4(self):
        self.assertRaises(TypeError, self.calculator.addition, [2, 3], {123, '3234'})

    def test_add_negative_5(self):
        self.assertRaises(TypeError, self.calculator.addition, ['asda', 34], None)

    # Next 6 tests check positive cases of subtraction function
    def test_subtraction_posititve(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtraction_posititve_1(self):
        self.assertEqual(self.calculator.subtraction(-1, 2), -3)

    def test_subtraction_posititve_2(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtraction_posititve_3(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

    def test_subtraction_posititve_4(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, math.inf), -math.inf)

    def test_subtraction_posititve_5(self):
        self.assertEqual(self.calculator.subtraction(0, 5.000001), -5.000001)

    # Next 8 tests check negative cases of subtraction function
    def test_subtraction_negative(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [2, 3], 'asdas')

    def test_subtraction_negative_1(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 0, 'asdas')

    def test_subtraction_negative_2(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [2, 3], '34, 43243, 4')

    def test_subtraction_negative_3(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [2, 3], 0.8)

    def test_subtraction_negative_4(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [2, 3], {123, '3234'})

    def test_subtraction_negative_5(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [2, 3], [123, '3234'])

    def test_subtraction_negative_6(self):
        self.assertRaises(TypeError, self.calculator.subtraction, '[2, 3], {123, \'3234\'}', '2342342')

    def test_subtraction_negative_7(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 'asdasd2')

    # Next 7 tests check positive cases of multiplication function
    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_positive_1(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiplication_positive_2(self):
        self.assertEqual(self.calculator.multiplication(0.9, 3), 2.7)

    def test_multiplication_positive_3(self):
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)

    def test_multiplication_positive_4(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.inf, 0)))

    def test_multiplication_positive_5(self):
        self.assertEqual(self.calculator.multiplication(math.inf, -math.inf), -math.inf)

    def test_multiplication_positive_6(self):
        self.assertEqual(self.calculator.multiplication(-2, -36.4), 72.8)

    # Next 5 tests check negative cases of multiplication function
    def test_multiplication_negative(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'asd', [2, 3])

    def test_multiplication_negative_1(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'asd', 'asdasd')

    def test_multiplication_negative_2(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 0.8, 'asdasd')

    def test_multiplication_negative_3(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, 8)

    def test_multiplication_negative_4(self):
        self.assertRaises(TypeError, self.calculator.multiplication, ['asd', 1], {32, 43})

    # Next 6 tests check positive cases of division function
    def test_division_positive(self):
        self.assertEqual(self.calculator.division(8, 2), 4)

    def test_division_positive_1(self):
        self.assertEqual(self.calculator.division(8, math.inf), 0)

    def test_division_positive_2(self):
        self.assertEqual(self.calculator.division(0, math.inf), 0)

    def test_division_positive_3(self):
        self.assertEqual(self.calculator.division(8.8, -1.1), -8)

    def test_division_positive_4(self):
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))

    def test_division_positive_5(self):
        self.assertEqual(self.calculator.division(0, 0), None)

    # Next 3 tests check negative cases of division function
    def test_division_negative(self):
        self.assertRaises(TypeError, self.calculator.division, 'sadas', math.inf)

    def test_division_negative_1(self):
        self.assertRaises(TypeError, self.calculator.division, None, 2.6)

    def test_division_negative_2(self):
        self.assertRaises(TypeError, self.calculator.division, [23, 43, 4], {'23423', 123})

    # Next 7 tests check positive cases of absolute function
    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(-2), 2)

    def test_absolute_positive_1(self):
        self.assertEqual(self.calculator.absolute(2), 2)

    def test_absolute_positive_2(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_positive_4(self):
        self.assertEqual(self.calculator.absolute(-2.3232), 2.3232)

    def test_absolute_positive_5(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)

    def test_absolute_positive_6(self):
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    # Next 4 tests check negative cases of absolute function
    def test_absolute_negative(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'sadasd')

    def test_absolute_negative_1(self):
        self.assertRaises(TypeError, self.calculator.absolute, ['23', 1])

    def test_absolute_negative_2(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_absolute_negative_3(self):
        self.assertRaises(TypeError, self.calculator.absolute, {'3223', '[3, 4]'})

    # Next 11 tests check positive cases of degree function
    def test_degree_positive(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_positive_1(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_positive_2(self):
        self.assertEqual(self.calculator.degree(16, 0.25), 2)

    def test_degree_positive_3(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_positive_4(self):
        self.assertEqual(self.calculator.degree(1, -1), 1)

    def test_degree_positive_5(self):
        self.assertEqual(self.calculator.degree(-1, 4), 1)

    def test_degree_positive_6(self):
        self.assertEqual(self.calculator.degree(-1, 0), 1)

    def test_degree_positive_7(self):
        self.assertEqual(self.calculator.degree(1.44, 0.5), 1.2)

    def test_degree_positive_8(self):
        self.assertEqual(self.calculator.degree(10, -2), 0.01)

    def test_degree_positive_9(self):
        self.assertEqual(self.calculator.degree(math.inf, 0), 1)

    def test_degree_positive_10(self):
        self.assertEqual(self.calculator.degree(math.inf, -math.inf), 0)

    # Next 4 tests check negative cases of degree function
    def test_degree_negative(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 1)

    def test_degree_negative_1(self):
        self.assertRaises(TypeError, self.calculator.degree, 4, 'dsaasd')

    def test_degree_negative_2(self):
        self.assertRaises(TypeError, self.calculator.degree, ['32,4 3,34', '43', 1], 0.4)

    def test_degree_negative_3(self):
        self.assertRaises(TypeError, self.calculator.degree, {'32', 32, 4}, -3223)

    # Next 4 tests check positive cases of ln function
    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(8), math.log(8))

    def test_ln_positive_1(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_positive_2(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_positive_3(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    # Next 6 tests check negative cases of ln function
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_negative_1(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_negative_2(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_negative_3(self):
        self.assertRaises(TypeError, self.calculator.ln, ['32, 4', 12])

    def test_ln_negative_4(self):
        self.assertRaises(TypeError, self.calculator.ln, '[32, 4, 12]')

    def test_ln_negative_5(self):
        self.assertRaises(TypeError, self.calculator.ln, {23, 4})

    # Next 5 tests check positive cases of log function
    def test_log_positive(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_log_positive_1(self):
        self.assertEqual(self.calculator.log(4.4, 4.4), 1)

    def test_log_positive_2(self):
        self.assertEqual(self.calculator.log(1, 9), 0)

    def test_log_positive_3(self):
        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)

    def test_log_positive_4(self):
        self.assertTrue(math.isnan(self.calculator.log(math.inf, math.inf)))

    # Next 8 tests check negative cases of log function
    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, 8, 0)

    def test_log_negative_1(self):
        self.assertRaises(ValueError, self.calculator.log, -8, 3)

    def test_log_negative_2(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -10)

    def test_log_negative_3(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)

    def test_log_negative_4(self):
        self.assertRaises(TypeError, self.calculator.log, None, 0)

    def test_log_negative_5(self):
        self.assertRaises(TypeError, self.calculator.log, 10, 'asdasd')

    def test_log_negative_6(self):
        self.assertRaises(TypeError, self.calculator.log, [3, 4, None], 0.9)

    def test_log_negative_7(self):
        self.assertRaises(TypeError, self.calculator.log, 132, {'32', 12})

    # Next 7 tests check positive cases of sqrt function
    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_positive_1(self):
        self.assertEqual(self.calculator.sqrt(1.69), 1.3)

    def test_sqrt_positive_2(self):
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_positive_4(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_positive_5(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_positive_6(self):
        self.assertEqual(self.calculator.sqrt(-169), 7.960204194457795e-16 + 13j)

    # Next 4 tests check negative cases of sqrt function
    def test_sqrt_negative(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_negative_1(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [23, 43, 4])

    def test_sqrt_negative_2(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'None')

    def test_sqrt_negative_3(self):
        self.assertRaises(TypeError, self.calculator.sqrt, {32, None})

    # Next 7 tests check positive cases of nth-root function
    def test_nth_root_positive(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)

    def test_nth_root_positive_1(self):
        self.assertEqual(self.calculator.nth_root(4, 0.5), 16)

    def test_nth_root_positive_2(self):
        self.assertEqual(self.calculator.nth_root(1, 3), 1)

    def test_nth_root_positive_3(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)

    def test_nth_root_positive_4(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)

    def test_nth_root_positive_5(self):
        self.assertEqual(self.calculator.nth_root(math.inf, math.inf), 1)

    def test_nth_root_positive_6(self):
        self.assertEqual(self.calculator.nth_root(64, -3), 0.25)

    # Next 6 tests check negative cases of nth-root function
    def test_nth_root_negative(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 0, -2)

    def test_nth_root_negative_1(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 0, 0)

    def test_nth_root_negative_2(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 0, None)

    def test_nth_root_negative_3(self):
        self.assertRaises(TypeError, self.calculator.nth_root, '32.9', 32.9)

    def test_nth_root_negative_4(self):
        self.assertRaises(TypeError, self.calculator.nth_root, ['32, ', 12], 32.2)

    def test_nth_root_negative_5(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 0, {'32, 4', None})


if __name__ == "__main__":
    unittest.main()
