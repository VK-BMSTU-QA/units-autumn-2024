import unittest
import math
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int_to_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_add_int_to_float(self):
        self.assertEqual(self.calculator.addition(1, 2.3), 3.3)
    
    def test_add_float_to_int(self):
        self.assertEqual(self.calculator.addition(1.3, 2), 3.3)
    
    def test_add_float_to_float(self):
        self.assertEqual(self.calculator.addition(1.2, 2.1), 3.3)

    def test_add_digit_to_string_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.addition(1, "a")
        self.assertEqual(str(context.exception), "unsupported operand type(s) for +: 'int' and 'str'")
    
    def test_add_string_to_digit_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.addition("a", 1)
        self.assertEqual(str(context.exception), "can only concatenate str (not \"int\") to str")
    
    def test_add_string_to_float_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.addition(1.01, "a")
        self.assertEqual(str(context.exception), "unsupported operand type(s) for +: 'float' and 'str'")
    
    def test_add_float_to_string_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.addition("a", 1.01)
        self.assertEqual(str(context.exception), "can only concatenate str (not \"float\") to str")

    def test_sub_int_to_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
    
    def test_sub_int_to_float(self):
        self.assertEqual(round(self.calculator.subtraction(1, 2.3), 1), -1.3)
    
    def test_sub_float_to_int(self):
        self.assertEqual(round(self.calculator.subtraction(1.3, 2), 1), -0.7)
    
    def test_sub_float_to_float(self):
        self.assertEqual(round(self.calculator.subtraction(1.2, 2.1), 1), -0.9)

    def test_sub_digit_to_string_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction(1, "a")
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'int' and 'str'")
    
    def test_sub_string_to_digit_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction("a", 1)
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'str' and 'int'")
    
    def test_sub_string_to_float_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction(1.01, "a")
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'float' and 'str'")
    
    def test_sub_float_to_string_error(self):
        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction("a", 1.01)
        self.assertEqual(str(context.exception), "unsupported operand type(s) for -: 'str' and 'float'")

    def test_multiplication_int_to_int(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
    
    def test_multiplication_float_to_int(self):
        self.assertEqual(self.calculator.multiplication(1.4, 2), 2.8)
    
    def test_multiplication_int_to_float(self):
        self.assertEqual(round(self.calculator.multiplication(3, 2.3), 2), 6.9)

    def test_multiplication_float_to_float(self):
        self.assertEqual(round(self.calculator.multiplication(3.3, 3.3), 2), 10.89)
    
    def test_multiplication_int_to_zero(self):
        self.assertEqual(self.calculator.multiplication(99, 0), 0)

    def test_multiplication_zero_to_int(self):
        self.assertEqual(self.calculator.multiplication(0, 190), 0)
    
    def test_multiplication_zero_to_float(self):
        self.assertEqual(self.calculator.multiplication(0, 12.330), 0)
    
    def test_multiplication_float_to_zero(self):
        self.assertEqual(self.calculator.multiplication(1.33, 0), 0)
    
    def test_multiplication_zero_to_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_division_int_by_int(self):
        self.assertEqual(self.calculator.division(10, 2), 5)
    
    def test_division_float_by_int(self):
        self.assertEqual(self.calculator.division(5.5, 2), 2.75)
    
    def test_division_int_by_float(self):
        self.assertEqual(self.calculator.division(10, 2.5), 4)
    
    def test_division_float_by_float(self):
        self.assertEqual(self.calculator.division(5.5, 2.5), 2.2)
    
   # def test_division_by_zero(self):
   #     with self.assertRaises(ZeroDivisionError):
    #        self.calculator.division(10, 0)

    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
    
    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_degree_int_to_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
    
    def test_degree_float_to_int(self):
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)
    
    def test_degree_int_to_float(self):
        self.assertEqual(self.calculator.degree(3, 2.5), 15.588457268119896)
    
    def test_degree_float_to_float(self):
        self.assertEqual(self.calculator.degree(2.5, 2.5), 9.882117688026186)

    # Тесты для ln (натуральный логарифм)
    def test_ln_positive(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
    
    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)
    
    def test_ln_zero_error(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln_negative_error(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_log_base_10(self):
        self.assertEqual(self.calculator.log(100, 10), 2)

    def test_log_base_2(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
    
    def test_log_base_float(self):
        self.assertEqual(self.calculator.log(9, 3), 2)
    
    def test_log_base_zero_error(self):
        with self.assertRaises(ValueError):
            self.calculator.log(10, 0)

    def test_sqrt_positive(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
    
    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    #def test_sqrt_negative_error(self):
    #    with self.assertRaises(ValueError):
    #        self.calculator.sqrt(-1)

    def test_nth_root_int(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
    
    def test_nth_root_float(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
    
    #def test_nth_root_negative(self):
    #    self.assertEqual(round(self.calculator.nth_root(-27, 3), 2), -3)
    
    #def test_nth_root_zero_error(self):
    #    with self.assertRaises(ValueError):
    #        self.calculator.nth_root(10, 0)

def division_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_division_int_by_int'))
    suite.addTest(TestCalculator('test_division_float_by_int'))
    suite.addTest(TestCalculator('test_division_int_by_float'))
    suite.addTest(TestCalculator('test_division_float_by_float'))
    suite.addTest(TestCalculator('test_division_by_zero'))
    return suite

def log_ln_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_ln_positive'))
    suite.addTest(TestCalculator('test_ln_one'))
    suite.addTest(TestCalculator('test_ln_zero_error'))
    suite.addTest(TestCalculator('test_ln_negative_error'))
    suite.addTest(TestCalculator('test_log_base_10'))
    suite.addTest(TestCalculator('test_log_base_2'))
    suite.addTest(TestCalculator('test_log_base_float'))
    suite.addTest(TestCalculator('test_log_base_zero_error'))
    return suite

def addition_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_add_int_to_int'))
    suite.addTest(TestCalculator('test_add_int_to_float'))
    suite.addTest(TestCalculator('test_add_float_to_int'))
    suite.addTest(TestCalculator('test_add_float_to_float'))
    suite.addTest(TestCalculator('test_add_string_to_digit_error'))
    suite.addTest(TestCalculator('test_add_digit_to_string_error'))
    suite.addTest(TestCalculator('test_add_string_to_float_error'))
    suite.addTest(TestCalculator('test_add_float_to_string_error'))


    return suite

def multiplication_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_multiplication_int_to_int'))
    suite.addTest(TestCalculator('test_multiplication_float_to_int'))
    suite.addTest(TestCalculator('test_multiplication_int_to_float'))
    suite.addTest(TestCalculator('test_multiplication_float_to_float'))
    suite.addTest(TestCalculator('test_multiplication_int_to_zero'))
    suite.addTest(TestCalculator('test_multiplication_zero_to_int'))
    suite.addTest(TestCalculator('test_multiplication_zero_to_float'))
    suite.addTest(TestCalculator('test_multiplication_float_to_zero'))
    suite.addTest(TestCalculator('test_multiplication_zero_to_zero'))

    return suite

def subtraction_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_sub_int_to_int'))
    suite.addTest(TestCalculator('test_sub_float_to_int'))
    suite.addTest(TestCalculator('test_sub_int_to_float'))
    suite.addTest(TestCalculator('test_sub_float_to_float'))
    suite.addTest(TestCalculator('test_sub_string_to_digit_error'))
    suite.addTest(TestCalculator('test_sub_digit_to_string_error'))
    suite.addTest(TestCalculator('test_sub_string_to_float_error'))
    suite.addTest(TestCalculator('test_sub_float_to_string_error'))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    print("Running addition tests:")
    runner.run(addition_suite())

    print("\nRunning multiplication tests:")
    runner.run(multiplication_suite())

    print("\nRunning subtraction tests:")
    runner.run(subtraction_suite())

    unittest.main()
