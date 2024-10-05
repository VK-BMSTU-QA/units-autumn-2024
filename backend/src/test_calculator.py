import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
    
    def tearDown(self):
        pass

    # Test suite addition

    def test_addition_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_addition_float(self):
        self.assertEqual(self.calculator.addition(0.5, 2.5), 3)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
    
    def test_addition_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.addition, 'a', 4)
    
    def test_addition_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    # Test suite multiplication

    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
    
    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(1.5, 2.5), 3.75)
    
    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 2.5), 0)
    
    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -4), 8)

    def test_dmultiplication_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.division, 'a', 'b')
    
    def test_dmultiplication_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    # Test suite subtraction

    def test_substruction_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
    
    def test_substruction_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(1.5, 2.3), -0.8)
    
    def test_substruction_negative(self):
        self.assertAlmostEqual(self.calculator.subtraction(-3, -4), 1)
    
    def test_substruction_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'a', 'b')
    
    def test_substruction_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    # Test suite division

    def test_division_int(self):
        self.assertEqual(self.calculator.division(4, 2), 2)

    def test_division_float(self):
        self.assertEqual(self.calculator.division(2.6, 1.3), 2)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(-6, -3), 2)   
    
    def test_division_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    
    # Test suite absolute
    
    def test_absolute_int(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(0.5), 0.5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-1), 1)
    
    def test_absolute_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'a')

    def test_absolute_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)
    
    # Test suite degree 

    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
    
    def test_degree_float(self):
        self.assertEqual(self.calculator.degree(0.25, 0.5), 0.5)
    
    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(0.25, 0), 1)
    
    def test_degree_negative_base(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
    
    def test_degree_negative_degree(self):
        self.assertEqual(self.calculator.degree(2, -3), 0.125)
    
    def test_degree_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.degree, 'a', 'b')

    def test_degree_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, None)

    # Test suite ln

    def test_ln_int(self):
        self.assertAlmostEqual(self.calculator.ln(3), 1.09861228)
    
    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(0.5), -0.69314718)
    
    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)
    
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)
    
    def test_ln_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')
    
    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    
    # Test suite log

    def test_log_int(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
    
    def test_log_float(self):
        self.assertAlmostEqual(self.calculator.log(0.5, 1.5), -1.70951129)
    
    def test_log_zero_body(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 9)
    
    def test_log_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 9, 0)
    
    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -1, 9)
    
    def test_log_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 'b')
    
    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

    # Test suite sqrt

    def test_sqrt_int(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.5), 0.70710678)
    
    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
    
    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-5), 2.23606797j)

    def test_sqrt_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)
    
    # Test suite nth_root

    def test_nth_root_int(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
    
    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.5, 0.9), 0.46293735)
    
    def test_nth_root_zero_base(self):
        self.assertEqual(self.calculator.nth_root(0, 1), 0)
    
    def test_nth_root_zero_root(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
    
    def test_nth_root_negative_base(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), 1j)

    def test_nth_root_negative_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(4, -2), 0.5)
    
    def test_nth_root_non_numeric(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 'b')
    
    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)



if __name__ == "__main__":
    unittest.main()
