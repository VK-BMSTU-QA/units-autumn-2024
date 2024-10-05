import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition_cases(self):
        self.assertEqual(self.calculator.addition(2, 3), 5)
        self.assertEqual(self.calculator.addition(10, -3), 7)
        self.assertEqual(self.calculator.addition(-2, -5), -7)
        self.assertEqual(self.calculator.addition(-3, 3), 0)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertAlmostEqual(self.calculator.addition(2.1, 3.7), 5.8, places=7)

    def test_multiplication_cases(self):
        self.assertEqual(self.calculator.multiplication(6, 9), 54)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)
        self.assertEqual(self.calculator.multiplication(0, -9), 0)
        self.assertEqual(self.calculator.multiplication(80, 0), 0)
        self.assertEqual(self.calculator.multiplication(-5, -4), 20)
        self.assertEqual(self.calculator.multiplication(-6, 7), -42)
        self.assertAlmostEqual(self.calculator.multiplication(-0.7, -1.5), 1.05, places=7)

    def test_subtraction_cases(self):
        self.assertEqual(self.calculator.subtraction(10, 3), 7)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(-10, 4), -14)
        self.assertEqual(self.calculator.subtraction(7, -8), 15)
        self.assertEqual(self.calculator.subtraction(-4, -5), 1)
        self.assertEqual(self.calculator.subtraction(-3.7, -1.2), -2.5)

    def test_division_cases(self):
        self.assertEqual(self.calculator.division(49, 7), 7)
        self.assertEqual(self.calculator.division(-45, 15), -3)
        self.assertEqual(self.calculator.division(-21, -3), 7)
        self.assertEqual(self.calculator.division(1.5, -0.5), -3)

    def test_absolute_cases(self):
        self.assertEqual(self.calculator.absolute(3), 3)
        self.assertEqual(self.calculator.absolute(-4), 4)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-0.47), 0.47)

    def test_exponentiation_cases(self):
        self.assertEqual(self.calculator.degree(2, 5), 32)
        self.assertEqual(self.calculator.degree(0, 50), 0)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertEqual(self.calculator.degree(2, 10), 1024)
        self.assertEqual(self.calculator.degree(-3, 4), 81)
        self.assertAlmostEqual(self.calculator.degree(3, -2), 1/9)

    def test_ln_cases(self):
        self.assertAlmostEqual(self.calculator.ln(3.8), 1.33500106673234)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(math.e ** 3), 3)
        self.assertAlmostEqual(self.calculator.ln(5.7), 1.7404661748405046)
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_logarithm_cases(self):
        self.assertAlmostEqual(self.calculator.log(512, 2), 9)
        self.assertAlmostEqual(self.calculator.log(81, 3), 4)
        self.assertAlmostEqual(self.calculator.log(25, 5), 2)
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)

    def test_sqrt_cases(self):
        self.assertAlmostEqual(self.calculator.sqrt(49), 7)
        self.assertAlmostEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(-144), 12j)

    def test_nth_root_cases(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)
        self.assertAlmostEqual(self.calculator.nth_root(0, 50), 0)
        self.assertAlmostEqual(self.calculator.nth_root(4, 0.5), 16)
        self.assertAlmostEqual(self.calculator.nth_root(-16, 2), 4j)

    def test_sqrt_of_negative_number(self):
        result = self.calculator.sqrt(-64)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result.imag, 8)

    def test_division_by_zero_exception(self):
        self.assertIsNone(self.calculator.division(10, 0))

    def test_ln_of_negative_number(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-5)

    def test_logarithm_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(150, 1)
        with self.assertRaises(ValueError):
            self.calculator.log(150, -3)
        with self.assertRaises(ValueError):
            self.calculator.log(150, 0)
        with self.assertRaises(ValueError):
            self.calculator.log(-150, 10)

    def test_nth_root_of_zero_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(15, 0)

    def test_addition_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.addition('hello', 3)
        with self.assertRaises(TypeError):
            self.calculator.addition([10, 20], 30)

    def test_multiplication_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication({}, 2)

    def test_subtraction_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('world', 1)
        with self.assertRaises(TypeError):
            self.calculator.subtraction([4, 5], 8)

    def test_division_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.division('test', 2)
        with self.assertRaises(TypeError):
            self.calculator.division([3, 4], 7)

    def test_absolute_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute('text')
        with self.assertRaises(TypeError):
            self.calculator.absolute([5, 6])

    def test_exponentiation_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('exp', 2)
        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], 3)

    def test_ln_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('log')
        with self.assertRaises(TypeError):
            self.calculator.ln([7, 8])

    def test_logarithm_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.log('logarithm', 2)
        with self.assertRaises(TypeError):
            self.calculator.log([2, 3], 4)

    def test_sqrt_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('square_root')
        with self.assertRaises(TypeError):
            self.calculator.sqrt([1, 9])

    def test_nth_root_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('root', 2)
        with self.assertRaises(TypeError):
            self.calculator.nth_root([7, 3], 2)

    def test_addition_with_unusual_type(self):
        self.assertEqual(self.calculator.addition('hi', 'world'), 'hiworld')
        self.assertEqual(self.calculator.addition([2, 3], [4, 5]), [2, 3, 4, 5])

    def test_multiplication_with_unusual_type(self):
        self.assertEqual(self.calculator.multiplication('abc', 3), 'abcabcabc')
        self.assertEqual(self.calculator.multiplication([2, 3], 2), [2, 3, 2, 3])

    def test_subtraction_with_unusual_type(self):
        self.assertEqual(self.calculator.subtraction({2, 3}, {3}), {2})

    def test_nth_root_complex_cases(self):
        result = self.calculator.nth_root(-81, 2)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result.imag, 9)

if __name__ == "__main__":
    unittest.main()