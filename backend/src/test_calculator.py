import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # addition tests
    def test_addition_integers(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition_integers_different_signs(self):
        self.assertEqual(self.calculator.addition(-2, 2), 0)
        
    def test_addition_float(self):
        self.assertAlmostEqual(self.calculator.addition(-2.2, 2), -0.2)

    def test_addition_float_different_signs(self):
        self.assertAlmostEqual(self.calculator.addition(-2.2, -2), -4.2)

    def test_addition_complex(self):
        self.assertAlmostEqual(self.calculator.addition((2.5 + 2.5j), (-2 + 2.2j)), 0.5 + 4.7j)

    def test_addition_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.addition, 'text', 1)

    # multiplication tests    
    def test_multiplication_integers(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 10), 0)

    def test_multiplication_different_signs(self):
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)
        
    def test_multiplication_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(-2.2, 2), -4.4)

    def test_multiplication_complex(self):
        self.assertAlmostEqual(self.calculator.multiplication((1.5 + 2j), (-2 + 2.2j)), -7.4 - 0.7j)

    def test_multiplication_wrong_type(self):
        self.assertEqual(self.calculator.multiplication('text', 1), 'text')

    # substracion tests
    def test_subtraction_integers(self):
        self.assertEqual(self.calculator.subtraction(3, 3), 0)

    def test_subtraction_defferent_signs(self):
        self.assertEqual(self.calculator.subtraction(6, -1), 7)

    def test_subtraction_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(-2.2, 2), -4.2)

    def test_subtraction_complex(self):
        self.assertAlmostEqual(self.calculator.subtraction((6.6 + 2j), (-3 + 2.2j)), 9.6 - 0.2j)

    def test_subtraction_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'text', 1)

    # division tests
    def test_division_integers(self):
        self.assertEqual(self.calculator.division(3, 3), 1)

    def test_division_different_signs(self):
        self.assertEqual(self.calculator.division(12, -4), -3)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(12, 0), None)

    def test_division_complex(self):
        self.assertAlmostEqual(self.calculator.division((1.5 + 2j), (-2 + 2.2j)), (0.15837104072398192-0.8257918552036199j))

    def test_division_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.division, 'text', 1)

    def test_division_zero(self):
        self.assertIsNone(self.calculator.division(3, 0))

    # absolute tests
    def test_absolute_integers(self):
        self.assertEqual(self.calculator.absolute(3), 3)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(-3.3), 3.3)

    def test_absolute_complex(self):
        self.assertAlmostEqual(self.calculator.absolute(1 - 1.35j), 1.68002976)

    def test_absolute_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'text')

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    # degree tests
    def test_degree_integers(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)

    def test_degree_float(self):
        self.assertAlmostEqual(self.calculator.degree(3.3, 2), 10.89)
    
    def test_degree_complex(self):
        self.assertAlmostEqual(self.calculator.degree(1 - 1.35j, 2), -0.8225 - 2.7j)

    def test_degree_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.degree, 'text', 1)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(3, 0), 1)

    # ln tests
    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_complex(self):
        self.assertRaises(TypeError, self.calculator.ln, 1j)

    def test_ln_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.ln, 'text')

    def test_ln_invalid(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    # log tests
    def test_log_positive(self):
        self.assertEqual(self.calculator.log(27, 3), 3)

    def test_log_complex(self):
        self.assertRaises(TypeError, self.calculator.log, 1j, 2)

    def test_log_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.log, 'text', 1)

    def test_log_wrong_base(self):
        self.assertRaises(ValueError, self.calculator.log, 1, -100)

    # sqrt tests
    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2), (8.659560562354934e-17+1.4142135623730951j))

    def test_sqrt_complex(self):
        self.assertAlmostEqual(self.calculator.sqrt(1j), 0.707106781 + 0.707106781j)

    def test_sqrt_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'text')

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
    

    # nth root tests
    def test_nth_root_positive(self):
        self.assertEqual(self.calculator.nth_root(128, 7), 2)

    def test_nth_root_negative(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, 2), (8.659560562354934e-17+1.4142135623730951j))

    def test_nth_root_complex(self):
        self.assertAlmostEqual(self.calculator.nth_root(1j, 2), 0.707106781 + 0.707106781j)

    def test_nth_root_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'text', 1)

    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 128, 0)


if __name__ == "main":
    unittest.main()
