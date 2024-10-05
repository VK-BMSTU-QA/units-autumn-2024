import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    ################################ +++++++++++++++++ ######################################

    def test_addition_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_float(self):
        self.assertEqual(self.calculator.addition(3.5, 3.5), 7)

    def test_addition_float_int(self):
        self.assertEqual(self.calculator.addition(3.5, 3), 6.5)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-15, -25), -40)

    def test_addition_negative_positive(self):
        self.assertEqual(self.calculator.addition(10, -20), -10)

    def test_addition_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.addition, 'z', 33)

    ################################ ******************** ######################################

    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(3.5, 3.5), 12.25)

    def test_multiplication_float_int(self):
        self.assertEqual(self.calculator.multiplication(3.5, 3), 10.5)

    def test_multiplication_zero_int(self):
        self.assertEqual(self.calculator.multiplication(0, 3), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-15, -25), 375)

    def test_multiplication_negative_positive(self):
        self.assertEqual(self.calculator.multiplication(10, -20), -200)

    def test_multiplication_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'z', 'y')

    ################################ --------------------- ######################################

    def test_subtraction_int(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtraction_float(self):
        self.assertEqual(self.calculator.subtraction(3.5, 3.5), 0)

    def test_subtraction_float_int(self):
        self.assertEqual(self.calculator.subtraction(3.5, 3), 0.5)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(-15, -25), 10)

    def test_subtraction_negative_positive(self):
        self.assertEqual(self.calculator.subtraction(10, -20), 30)

    def test_subtraction_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'z', 'x')

    ################################ ///////////////////// ######################################

    def test_division_int(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_float_float(self):
        self.assertEqual(self.calculator.division(2.5, 0.5), 5)

    def test_division_float_int(self):
        self.assertEqual(self.calculator.division(10.5, 3), 3.5)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_division_negative_negative(self):
        self.assertEqual(self.calculator.division(-10, -5), 2)

    def test_division_negative_positive(self):
        self.assertEqual(self.calculator.division(-10, 5), -2)

    def test_division_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.division, 'z', 'y')

    ################################ |abs| ######################################

    def test_absolute_int(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(5.5), 5.5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_absolute_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'z')

    ################################ degree ######################################

    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_float_float(self):
        self.assertEqual(self.calculator.degree(0.25, 0.5), 0.5)

    def test_degree_float_int(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(10, 0), 1)

    def test_degree_negative_base_even(self):
        self.assertEqual(self.calculator.degree(-4, 2), 16)

    def test_degree_negative_base_uneven(self):
        self.assertEqual(self.calculator.degree(-4, 3), -64)

    def test_degree_negative_degree_even(self):
        self.assertEqual(self.calculator.degree(10, -4), 0.0001)

    def test_degree_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.degree, 'z', 'x')

    ################################ ln ######################################

    def test_ln_int(self):
        self.assertAlmostEqual(self.calculator.ln(2), 0.6931471805599453)

    def test_ln_float_more_than_1(self):
        self.assertAlmostEqual(self.calculator.ln(2.5), 0.91629073187)

    def test_ln_float_less_than_1(self):
        self.assertAlmostEqual(self.calculator.ln(0.1), (-2.30258509299))

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.ln, 'z')

    ################################ log ######################################

    def test_log_int(self):
        self.assertAlmostEqual(self.calculator.log(16, 2), 4)

    def test_log_float_float(self):
        self.assertAlmostEqual(self.calculator.log(1.2, 2.4), 0.2082559308114424)

    def test_log_float_int(self):
        self.assertAlmostEqual(self.calculator.log(5, 2.5), 1.7564707973660298)

    def test_log_zero_body(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 33)

    def test_log_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 33, 0)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -25, 125)

    def test_log_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.log, 'z', 'x')

    ################################ sqrt ######################################

    def test_sqrt_int(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.4), 1.5491933384829668)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2), 8.659560562354934e-17+1.4142135623730951j)

    def test_sqrt_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'z')

    ################################ root ######################################

    def test_nth_root_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(64, 3), 4)

    def test_nth_root_float_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.75, 0.75), 0.6814202223120523)

    def test_nth_root_int_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(75, 0.75),  316.28724948815585)

    def test_nth_root_zero_base(self):
        self.assertEqual(self.calculator.nth_root(0, 1), 0)

    def test_nth_root_zero_root(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)

    def test_nth_root_negative_base(self):
        self.assertAlmostEqual(self.calculator.nth_root(-3, 6), 1.040041911525952+0.6004684775880013j)

    def test_nth_root_negative_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(3, -6), 0.8326831776556043)

    def test_nth_root_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'z', 'x')


if __name__ == "__main__":
    unittest.main()
