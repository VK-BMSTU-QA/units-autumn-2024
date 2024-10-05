import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_1(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calculator.addition(2381, 1015), 3396)

    def test_add_3(self):
        self.assertEqual(self.calculator.addition(0, -0), 0)

    def test_add_4(self):
        self.assertEqual(self.calculator.addition(+math.inf, 0), +math.inf)

    def test_add_5(self):
        self.assertEqual(self.calculator.addition(-math.inf, 0), -math.inf)

    def test_add_6(self):
        result = self.calculator.addition(-math.inf, +math.inf)
        self.assertTrue(math.isnan(result))

    def test_add_7(self):
        self.assertEqual(self.calculator.addition(0.00001, 0), 0.00001)

    def test_add_8(self):
        self.assertEqual(self.calculator.addition('', ''), '')

    def test_add_9(self):
        self.assertEqual(self.calculator.addition('', 'good_data'), 'good_data')

    def test_add_10(self):
        self.assertEqual(self.calculator.addition(345.386345, 2.22222), 347.608565)

    def test_add_11(self):
        self.assertEqual(self.calculator.addition(345.386345, -2.22222), 343.164125)

    def test_add_12(self):
        self.assertEqual(self.calculator.addition(-123.823, +24), -99.823)

    def test_addition_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(1, 'a')

    def test_multiplication_1(self):
        self.assertEqual(self.calculator.multiplication(1124, 0), 0)

    def test_multiplication_2(self):
        self.assertEqual(self.calculator.multiplication(1, 1.000001), 1.000001)

    def test_multiplication_3(self):
        self.assertEqual(self.calculator.multiplication(1, -1.000001), -1.000001)

    def test_multiplication_4(self):
        self.assertEqual(self.calculator.multiplication(-1, -1), 1)

    def test_multiplication_5(self):
        self.assertEqual(self.calculator.multiplication(-1, -1.000001), 1.000001)

    def test_multiplication_6(self):
        self.assertEqual(self.calculator.multiplication(1421, 642), 912282)

    def test_multiplication_7(self):
        self.assertEqual(self.calculator.multiplication(1421, -642), -912282)

    def test_multiplication_8(self):
        self.assertEqual(self.calculator.multiplication(1462.238, 642), 938756.7960000001)

    def test_multiplication_9(self):
        self.assertEqual(self.calculator.multiplication(-1462.238, 642), -938756.7960000001)

    def test_multiplication_10(self):
        self.assertEqual(self.calculator.multiplication('word', 4), 'wordwordwordword')

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(1124, 0), None)

    def test_division_2(self):
        self.assertEqual(self.calculator.division(1.000001, 1), 1.000001)

    def test_division_3(self):
        self.assertEqual(self.calculator.division(-1.000001, 1), -1.000001)

    def test_division_4(self):
        self.assertEqual(self.calculator.division(-1125, -1125), 1)

    def test_division_5(self):
        self.assertEqual(self.calculator.division(-1125, 1125), -1)

    def test_division_6(self):
        self.assertEqual(self.calculator.division(1421, 642), 2.2133956386292835)

    def test_division_7(self):
        self.assertEqual(self.calculator.division(1462, -642), -2.277258566978193)

    def test_division_8(self):
        self.assertEqual(self.calculator.division(1462.5, 642), 2.27803738317757)

    def test_division_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.division(1, 'a')

    def test_subtraction_1(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_subtraction_2(self):
        self.assertEqual(self.calculator.subtraction(2381, 1015), 1366)

    def test_subtraction_3(self):
        self.assertEqual(self.calculator.subtraction(0, -0), 0)

    def test_subtraction_4(self):
        self.assertEqual(self.calculator.subtraction(+math.inf, 0), +math.inf)

    def test_subtraction_5(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, 0), -math.inf)

    def test_subtraction_6(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, +math.inf), -math.inf)

    def test_subtraction_7(self):
        self.assertEqual(self.calculator.subtraction(0.00001, 0), 0.00001)

    def test_subtraction_8(self):
        self.assertEqual(self.calculator.subtraction(345.386345, 2.22222), 343.164125)

    def test_subtraction_9(self):
        self.assertEqual(self.calculator.subtraction(345.386345, -2.22222), 347.608565)

    def test_subtraction_10(self):
        self.assertEqual(self.calculator.subtraction(-123.823, +24), -147.82299999999998)

    def test_subtraction_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(1, 'a')

    def test_absolute_1(self):
        self.assertEqual(self.calculator.absolute(-0), 0)

    def test_absolute_2(self):
        self.assertEqual(self.calculator.absolute(14215), 14215)

    def test_absolute_3(self):
        self.assertEqual(self.calculator.absolute(-14215), 14215)

    def test_absolute_4(self):
        self.assertEqual(self.calculator.absolute(2421.7452), 2421.7452)

    def test_absolute_5(self):
        self.assertEqual(self.calculator.absolute(-2421.7452), 2421.7452)

    def test_absolute_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute('a')

    def test_degree_1(self):
        self.assertEqual(self.calculator.degree(1, -0), 1)

    def test_degree_2(self):
        self.assertEqual(self.calculator.degree(12412, 0), 1)

    def test_degree_3(self):
        self.assertEqual(self.calculator.degree(124, 1), 124)

    def test_degree_4(self):
        self.assertEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_5(self):
        self.assertEqual(self.calculator.degree(16, 1.5), 64)

    def test_degree_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(1, 'a')

    def test_ln_1(self):
        self.assertEqual(self.calculator.ln(1), 0.0)

    def test_ln_2(self):
        self.assertEqual(self.calculator.ln(12412), 9.42641902556827)

    def test_ln_3(self):
        self.assertEqual(self.calculator.ln(124.15157), 4.8215031578669665)

    def test_ln_4(self):
        self.assertEqual(self.calculator.ln(2), 0.6931471805599453)

    def test_ln_5(self):
        self.assertEqual(self.calculator.ln(16), 2.772588722239781)

    def test_ln_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_ln_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('a')

    def test_log_2(self):
        self.assertEqual(self.calculator.log(12412, 24), 2.9660979734053874)

    def test_log_3(self):
        self.assertEqual(self.calculator.log(124.15157, 4), 3.4779793477425747)

    def test_log_4(self):
        self.assertEqual(self.calculator.log(2, 0.15), -0.3653681296292077)

    def test_log_negative_value(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.log(1, 'a')

    def test_sqrt_1(self):
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_2(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_3(self):
        self.assertEqual(self.calculator.sqrt(124.15157), 11.142332341121405)

    def test_sqrt_4(self):
        self.assertEqual(self.calculator.sqrt(2), 1.4142135623730951)

    def test_sqrt_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('a')

    def test_nth_root_1(self):
        self.assertEqual(self.calculator.nth_root(1, 1), 1)

    def test_nth_root_2(self):
        self.assertEqual(self.calculator.nth_root(16, 2), 4)

    def test_nth_root_3(self):
        self.assertEqual(self.calculator.nth_root(124.15157, 10), 1.6195532114211464)

    def test_nth_root_4(self):
        self.assertEqual(self.calculator.nth_root(2, 4), 1.189207115002721)

    def test_nth_root_invalid_type_1(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('word', 2)

    def test_nth_root_invalid_type_2(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root(1, 'a')


if __name__ == "__main__":
    unittest.main()
