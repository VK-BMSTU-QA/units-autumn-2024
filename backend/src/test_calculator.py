import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # test add

    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        
    def test_add_float(self):
        self.assertEqual(self.calculator.addition(1.5, 2.), 3.5)
    
    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)
    
    def test_add_str(self):
        self.assertRaises(TypeError, self.calculator.addition, 'abc', 4)
        
    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(float('inf'), float('inf')), float('inf'))
    
    def test_add_inf_sign(self):
        self.assertTrue(math.isnan(self.calculator.addition(float('inf'), float('-inf'))))
    
    def test_add_neg(self):
        self.assertEqual(self.calculator.addition(-2, -4), -6)
        
    # test multiplication
    
    def test_mult_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
    
    def test_mult_float(self):
        self.assertEqual(self.calculator.multiplication(2.5, 3.5), 8.75)
    
    def test_mult_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)
    
    def test_mult_str(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'abc', 'asd')
    
    def test_mult_inf(self):
        self.assertEqual(self.calculator.multiplication(float('inf'), 2), float('inf'))
    
    def test_mult_inf_sign(self):
        self.assertEqual(self.calculator.multiplication(float('inf'), float('-inf')), float('-inf'))
    
    def test_mult_neg(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)
    
    def test_mult_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        
    def test_mult_zero2(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
    
    # test subtraction
    
    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(2, 3), -1)
        
    def test_sub_float(self):
        self.assertEqual(self.calculator.subtraction(2.4, 3.5), -1.1)
    
    def test_sub_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)
    
    def test_sub_str(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'abc', 'asd')
    
    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(float('inf'), 2), float('inf'))
    
    def test_sub_inf_sign(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(float('inf'), float('inf'))))
    
    def test_sub_neg(self):
        self.assertEqual(self.calculator.subtraction(-2, -3), 1)
    
    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 2), -2)
    
    def test_sub_zero2(self):
        self.assertEqual(self.calculator.subtraction(2, 0), 2)
    
    # test division
    
    def test_div_int(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
    
    def test_div_float(self):
        self.assertEqual(self.calculator.division(4.5, 2), 2.25)
    
    def test_div_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)
    
    def test_div_str(self):
        self.assertRaises(TypeError, self.calculator.division, 'abc', 'asd')
    
    def test_div_inf(self):
        self.assertEqual(self.calculator.division(float('inf'), 2), float('inf'))
    
    def test_div_inf_sign(self):
        self.assertTrue(math.isnan(self.calculator.division(float('inf'), float('inf'))))
    
    def test_div_neg(self):
        self.assertEqual(self.calculator.division(-4, -2), 2)
    
    def test_div_zero(self):
        self.assertEqual(self.calculator.division(0, 2), 0)
    
    def test_div_zero2(self):
        self.assertEqual(self.calculator.division(2, 0), None)
    
    # test absolute
    
    def test_abs_int_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)
    
    def test_abs_int_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
    
    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)
    
    def test_abs_float_positive(self):
        self.assertEqual(self.calculator.absolute(5.5), 5.5)
    
    def test_abs_float_negative(self):
        self.assertEqual(self.calculator.absolute(-5.5), 5.5)
    
    def test_abs_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)
    
    def test_abs_str(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'abc')
    
    def test_abs_inf(self):
        self.assertEqual(self.calculator.absolute(float('inf')), float('inf'))
    
    def test_abs_inf_sign(self):
        self.assertEqual(self.calculator.absolute(float('-inf')), float('inf'))
    
    # test degree

    def test_degree_positive_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_negative_int(self):
        self.assertEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_neg_base(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_zero_exponent(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree_positive_float(self):
        self.assertAlmostEqual(self.calculator.degree(2, 0.5), math.sqrt(2))

    def test_degree_negative_float(self):
        self.assertAlmostEqual(self.calculator.degree(2, -0.5), 1 / math.sqrt(2))

    def test_degree_zero_base(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    def test_degree_one_base(self):
        self.assertEqual(self.calculator.degree(1, 5), 1)

    def test_degree_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    def test_degree_str(self):
        self.assertRaises(TypeError, self.calculator.degree, 'abc', 2)

    def test_degree_inf_base(self):
        self.assertEqual(self.calculator.degree(float('inf'), 2), float('inf'))
    
    def test_degree_inf_sign(self):
        self.assertEqual(self.calculator.degree(float('inf'), -2), 0)
    
    def test_degree_inf_exponent(self):
        self.assertEqual(self.calculator.degree(2, float('inf')), float('inf'))
    
    def test_degree_inf_exponent_sign(self):
        self.assertEqual(self.calculator.degree(2, float('-inf')), 0)
        
    def test_degree_inf_base_exponent(self):
        self.assertEqual(self.calculator.degree(float('inf'), float('inf')), float('inf'))
    
    def test_degree_inf_base_neg_exponent(self):
        self.assertEqual(self.calculator.degree(float('inf'), float('-inf')), 0)
    
    def test_degree_inf_base_neg_inf_exponent(self):
        self.assertEqual(self.calculator.degree(float('-inf'), float('inf')), float('inf'))
    
    def test_degree_inf_base_neg_neg_inf_exponent(self):
        self.assertEqual(self.calculator.degree(float('-inf'), float('-inf')), 0)
        
    # test ln

    def test_ln_positive_int(self):
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))

    def test_ln_positive_float(self):
        self.assertAlmostEqual(self.calculator.ln(2.5), math.log(2.5))

    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -2)

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_str(self):
        self.assertRaises(TypeError, self.calculator.ln, 'abc')
    
    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))
    
    def test_ln_neg_inf(self):
        self.assertRaises(ValueError, self.calculator.ln, float('-inf'))
    
    # test log
    
    def test_log_positive_int(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_positive_float(self):
        self.assertAlmostEqual(self.calculator.log(8.0, 2.0), 3)

    def test_log_base_one(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 8, 1)

    def test_log_base_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 8, 0)

    def test_log_negative_base(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -2)

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    def test_log_str(self):
        self.assertRaises(TypeError, self.calculator.log, 'abc', 2)

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(float('inf'), 2), float('inf'))

    def test_log_neg_inf(self):
        self.assertRaises(ValueError, self.calculator.log, 8, float('-inf'))
    
    def test_log_neg_inf_base(self):
        self.assertRaises(ValueError, self.calculator.log, float('-inf'), 2)
    
    # test sqrt
    
    def test_sqrt_positive_int(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_positive_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(4.0), 2.0)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-4), (0 + 2j))

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_str(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'abc')

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(float('inf')), float('inf'))

    def test_sqrt_neg_inf(self):
        self.assertEqual(self.calculator.sqrt(float('-inf')), float('inf'))

    # test nth_root
    
    def test_nth_root_positive_int(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)

    def test_nth_root_positive_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(27.0, 3.0), 3.0)

    def test_nth_root_one(self):
        self.assertEqual(self.calculator.nth_root(27, 1), 27)

    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 27, 0)

    def test_nth_root_negative(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, -3), 1 / 3)

    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 3)

    def test_nth_root_str(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'abc', 3)

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), 3), float('inf'))

    def test_nth_root_neg_inf(self):
        self.assertEqual(self.calculator.nth_root(float('-inf'), 3), float('inf'))
    
    def test_nth_root_inf_exponent(self):
        self.assertEqual(self.calculator.nth_root(27, float('inf')), 1)
    
    def test_nth_root_inf_neg_exponent(self):
        self.assertEqual(self.calculator.nth_root(27, float('-inf')), 1)
        
    def test_nth_root_inf_base_inf_exponent(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), float('inf')), 1)
    
    def test_nth_root_inf_base_neg_inf_exponent(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), float('-inf')), 1)
    
    def test_nth_root_neg_inf_base_neg_inf_exponent(self):
        self.assertEqual(self.calculator.nth_root(float('-inf'), float('-inf')), 1)
    
    def test_nth_root_neg_inf_base_inf_exponent(self):
        self.assertEqual(self.calculator.nth_root(float('-inf'), float('inf')), 1)

if __name__ == "__main__":
    unittest.main()
