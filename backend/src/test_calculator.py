import unittest
from src.calculator import Calculator
import math

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # test_add
    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(-1, -1), -2)

    def test_add_floats(self):
        self.assertEqual(self.calculator.addition(1.3, 2.5), 3.8)

    def test_add_strings(self):
        self.assertRaises(TypeError, self.calculator.addition, "1", 2)
   
    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, 1)

    def test_add_complex_numbers(self):
        self.assertEqual(self.calculator.addition(1 + 2j, 3 + 4j), 4 + 6j)
      
    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, -1), -math.inf)


    # test_mult
    def test_mult_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_mult_by_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 4), 0)

    def test_mult_floats(self):
        self.assertEqual(self.calculator.multiplication(1.3, -2.5), -3.25)

    def test_mult_strings(self):
        self.assertEqual(self.calculator.multiplication("1", 2), "11")
   
    def test_mult_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, 1)

    def test_mult_complex_numbers(self):
        self.assertEqual(self.calculator.multiplication(1 + 2j, 3 + 4j), -5 + 10j)

    def test_mult_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, -1), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, 1), -math.inf)


    # test_sub
    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertEqual(self.calculator.subtraction(1, 1), 0)
        self.assertEqual(self.calculator.subtraction(-1, -1), 0)

    def test_sub_floats(self):
        self.assertEqual(self.calculator.subtraction(1.3, -2.5), 3.8)
        self.assertEqual(self.calculator.subtraction(-1.3, 2.5), -3.8)

    def test_sub_strings(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "1", 2)
   
    def test_sub_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    def test_sub_complex_numbers(self):
        self.assertEqual(self.calculator.subtraction(1 + 2j, 3 + 4j), -2 - 2j)
    
    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, -1), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 1), -math.inf)

    # test_div
    def test_div_int(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(-6, -3), 2)
        self.assertEqual(self.calculator.division(-6, 3), -2)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(4, 0), None)  

    def test_div_floats(self):
        self.assertEqual(self.calculator.division(7.5, 2.5), 3.0)

    def test_div_strings(self):
        self.assertRaises(TypeError, self.calculator.division, "6", 3)

    def test_div_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, 2)

    def test_div_complex_numbers(self):
        self.assertEqual(self.calculator.division(1 + 2j, 1 + 1j), (1.5 + 0.5j))
    
    def test_div_inf(self):
        self.assertEqual(self.calculator.division(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, -1), math.inf)
        self.assertEqual(self.calculator.division(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 1), -math.inf)
  
    # test_abs
    def test_abs_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_float(self):
        self.assertEqual(self.calculator.absolute(-3.5), 3.5)

    def test_abs_complex(self):
        self.assertEqual(self.calculator.absolute(3 + 4j), 5.0)  
      
    def test_abs_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)
   
    def test_abs_str(self):
        self.assertRaises(TypeError, self.calculator.absolute, '1')
    
    def test_abs_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    # test_deg
    def test_deg_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_deg_negative_exponent(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_deg_float(self):
        self.assertEqual(self.calculator.degree(1.5, 2), 2.25)

    def test_deg_zero_base(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    def test_deg_zero_exponent(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_deg_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, 10), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 5), -math.inf)

    def test_deg_base_is_string(self):
        self.assertRaises(TypeError, self.calculator.degree, '1', 2)

    def test_deg_exponent_is_string(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, '1')

    def test_deg_base_is_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    def test_deg_exponent_is_none(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)

    # test_ln
    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_of_e(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)  

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)  
        
    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    def test_ln_str(self):
        self.assertRaises(TypeError, self.calculator.ln, '1')

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    # test_log
    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log_one(self):
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)

    def test_log_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -10, 10)
      
    def test_log_inf(self):
        self.assertEqual(self.calculator.log(math.inf, 10), math.inf)

    def test_log_str(self):
        self.assertRaises(TypeError, self.calculator.log, '1', 2)

    def test_log_base_str(self):
        self.assertRaises(TypeError, self.calculator.log, 2, '1')

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    def test_log_base_none(self):
        self.assertRaises(TypeError, self.calculator.log, 2, None)

    # test_sqrt
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.25), 1.5)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_sqrt_str(self):
        self.assertRaises(TypeError, self.calculator.sqrt, '1')

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    # test_nth_root
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 3), 0)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(16.0, 4), 2.0)
      
    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
    
    def test_nth_root_str(self):
        self.assertRaises(TypeError, self.calculator.nth_root, '1', 3)

    def test_nth_root_degree_str(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, '1')

    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)

    def test_nth_root_degree_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 2, None)


if __name__ == "__main__":
    unittest.main()
