import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(1, 1), 2)
        self.assertEqual(self.calculator.addition(3.4, 3.2), 6.6)
        self.assertEqual(self.calculator.addition(2, 2.1), 4.1)
        self.assertEqual(self.calculator.addition(-1, -1), -2)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(-1, 0), -1)
        self.assertEqual(self.calculator.addition(1, -1), 0)
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)
        with self.assertRaises(TypeError):
            self.calculator.addition('hh', [1, 2]) 

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(1, 1), 0)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
        self.assertEqual(self.calculator.subtraction(-2, 1), -3)
        self.assertEqual(self.calculator.subtraction(2, -1), 3)
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
        self.assertEqual(self.calculator.subtraction(2.6, 1.1), 1.5)
        with self.assertRaises(TypeError):
            self.calculator.subtraction('hh', 'f') 

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(2, 1), 2)
        self.assertEqual(self.calculator.multiplication(2, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(2, -3), -6)
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)
        self.assertEqual(self.calculator.multiplication(2.4, 3.4), 8.16)
        with self.assertRaises(TypeError):
            self.calculator.multiplication('hh', 'f') 

    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(4, 1), 4)
        self.assertEqual(self.calculator.division(0, 2), 0)
        self.assertEqual(self.calculator.division(4, -2), -2)
        self.assertEqual(self.calculator.division(-4, 2), -2)
        self.assertEqual(self.calculator.division(-4, -2), 2)
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(4.2, 2), 2.1)
        self.assertEqual(self.calculator.division(5, 2.5), 2)
        with self.assertRaises(TypeError):
            self.calculator.division('hh', 'f') 
        self.assertIsNone(self.calculator.division(34, 0))

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-4), 4)
        self.assertEqual(self.calculator.absolute(4.3), 4.3)
        self.assertEqual(self.calculator.absolute(-4.8), 4.8)
        with self.assertRaises(TypeError):
            self.calculator.absolute('hh') 

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)
        self.assertEqual(self.calculator.degree(4, 1), 4)
        self.assertEqual(self.calculator.degree(4, 0), 1)
        self.assertEqual(self.calculator.degree(4, -1), 0.25)
        self.assertEqual(self.calculator.degree(-4, 3), -64)
        self.assertEqual(self.calculator.degree(-4, 2), 16)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertAlmostEqual(self.calculator.degree(4.2, 3), 74.088)
        with self.assertRaises(TypeError):
            self.calculator.degree('hh', 'f') 

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(math.e ** 3), 3)
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(2.8), 1.02961942)
        with self.assertRaises(TypeError):
            self.calculator.ln('hh') 
        with self.assertRaises(ValueError):
            self.calculator.ln(0) 
        with self.assertRaises(ValueError):
            self.calculator.ln(-10) 

    def test_log(self):
        self.assertEqual(self.calculator.log(9, 3), 2)
        self.assertEqual(self.calculator.log(1, 3), 0)
        self.assertEqual(self.calculator.log(9, 9), 1)
        self.assertAlmostEqual(self.calculator.log(2.8, 1.4), 3.0600427)
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
        with self.assertRaises(TypeError):
            self.calculator.log('hh', 'f') 

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(16), 4)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)
        self.assertAlmostEqual(self.calculator.sqrt(4.5), 2.12132034)
        with self.assertRaises(TypeError):
            self.calculator.sqrt('hh') 

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(0, 3), 0)
        self.assertEqual(self.calculator.nth_root(1, 3), 1)
        self.assertEqual(self.calculator.nth_root(15, 1), 15)  
        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), 1j)    
        self.assertAlmostEqual(self.calculator.nth_root(27.5, 4), 2.2899878)
        self.assertAlmostEqual(self.calculator.nth_root(27, 4.5), 2.0800838)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(27, 0)  
        with self.assertRaises(TypeError):
            self.calculator.nth_root('hh', 'f') 
        

if __name__ == "__main__":
    unittest.main()
