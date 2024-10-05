import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(1, 1), 2)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, -1), -2)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(1, -1), 0)

    def test_addition_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(-1, 0), -1)

    def test_addition_float(self):
        self.assertEqual(self.calculator.addition(3.4, 3.2), 6.6)
        self.assertEqual(self.calculator.addition(2, 2.1), 4.1)

    def test_addition_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_addition_error(self):
        with self.assertRaises(TypeError):
            self.calculator.addition('hh', [1, 2]) 


    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(1, 1), 0)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(-2, 1), -3)
        self.assertEqual(self.calculator.subtraction(2, -1), 3)
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)

    def test_subtraction_float(self):
        self.assertEqual(self.calculator.subtraction(2.6, 1.1), 1.5)

    def test_subtraction_error(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('hh', 'f') 


    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(2, 1), 2)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(2, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(2, -3), -6)
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(2.4, 3.4), 8.16)

    def test_multiplication_error(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication('hh', 'f') 

    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(4, 1), 4)
        self.assertEqual(self.calculator.division(0, 2), 0)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(4, -2), -2)
        self.assertEqual(self.calculator.division(-4, 2), -2)
        self.assertEqual(self.calculator.division(-4, -2), 2)

    def test_division_float(self):
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(4.2, 2), 2.1)
        self.assertEqual(self.calculator.division(5, 2.5), 2)

    def test_division_error(self):
        with self.assertRaises(TypeError):
            self.calculator.division('hh', 'f') 

    def test_division_on_zero(self):
        self.assertIsNone(self.calculator.division(34, 0))

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-4), 4)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(4.3), 4.3)
        self.assertEqual(self.calculator.absolute(-4.8), 4.8)

    def test_absolute_error(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute('hh') 

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)
        self.assertEqual(self.calculator.degree(4, 1), 4)
        self.assertEqual(self.calculator.degree(4, 0), 1)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(4, -1), 0.25)
        self.assertEqual(self.calculator.degree(-4, 3), -64)
        self.assertEqual(self.calculator.degree(-4, 2), 16)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 2), 0)

    def test_degree_one(self):
        self.assertEqual(self.calculator.degree(1, 2), 1)

    def test_degree_float(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertAlmostEqual(self.calculator.degree(4.2, 3), 74.088)

    def test_degree_error(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('hh', 'f') 

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(math.e ** 3), 3)
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(2.8), 1.02961942)

    def test_ln_wrong_values(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0) 
        with self.assertRaises(ValueError):
            self.calculator.ln(-10) 

    def test_ln_error(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('hh') 

    def test_log(self):
        self.assertEqual(self.calculator.log(9, 3), 2)
        self.assertEqual(self.calculator.log(1, 3), 0)
        self.assertEqual(self.calculator.log(9, 9), 1)

    def test_log_float(self):
        self.assertAlmostEqual(self.calculator.log(2.8, 1.4), 3.0600427)

    def test_log_wrong_values(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(100, 1)
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)
        with self.assertRaises(ValueError):
            self.calculator.log(10, 0)
        with self.assertRaises(ValueError):
            self.calculator.log(10, -10)
        with self.assertRaises(ValueError):
            self.calculator.log(-10, 10)

    def test_log_error(self):
        with self.assertRaises(TypeError):
            self.calculator.log('hh', 'f') 

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_complex(self):
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(4.5), 2.12132034)

    def test_sqrt_error(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('hh') 

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(0, 3), 0)
        self.assertEqual(self.calculator.nth_root(1, 3), 1)
        self.assertEqual(self.calculator.nth_root(15, 1), 15)  
        
    def test_nth_root_complex(self):
        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), 1j) 

    def test_nth_root_float(self):   
        self.assertAlmostEqual(self.calculator.nth_root(27.5, 4), 2.2899878)
        self.assertAlmostEqual(self.calculator.nth_root(27, 4.5), 2.0800838)

    def test_nth_root_wrong_values(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(27, 0)  

    def test_nth_root_error(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('hh', 'f') 

if __name__ == "__main__":
    unittest.main()
