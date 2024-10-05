import math
import unittest

from src.calculator import Calculator


class TestCalculatorAdd(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_negative_positive(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)

    def test_add_string_num(self):
        self.assertRaises(TypeError, self.calculator.addition, '1', 1)

    def test_add_none_num(self):
        self.assertRaises(TypeError, self.calculator.addition, None, 1)

    def test_add_float(self):
        self.assertEqual(self.calculator.addition(1.5, 2.5), 4)

    def test_add_big(self):
        self.assertEqual(self.calculator.addition(5e10, 6e10), 1.1e11) # больше нет смысла, потому что там уже проблемы представления больших чисел

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)

    def test_add_inf2(self):
        self.assertEqual(self.calculator.addition(-math.inf, 1), -math.inf)

class TestCalculatorMulti(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_multi_pos(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_multi_pos_neg(self):
        self.assertEqual(self.calculator.multiplication(1, -2), -2)

    def test_multi_neg_neg(self):
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)

    def test_multi_pos_zero(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)

    def test_multi_pos_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 1, None)

    def test_multi_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)

class TestCalculatorSub(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()   

    def test_sub_positive(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)

    def test_sub_negative_positive(self):
        self.assertEqual(self.calculator.subtraction(-1, 2), -3)

    def test_sub_string_num(self):
        self.assertRaises(TypeError, self.calculator.subtraction, '1', 1)

    def test_sub_none_num(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    def test_sub_float(self):
        self.assertEqual(self.calculator.subtraction(1.5, 2.5), -1)

    def test_sub_big(self):
        self.assertEqual(self.calculator.subtraction(5e10, 6e10), -1e10)

    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)

    def test_sub_inf2(self):
        self.assertEqual(self.calculator.subtraction(-math.inf, 1), -math.inf)

class TestCalculatorDiv(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_div_pos(self):
        self.assertEqual(self.calculator.division(1, 2), 1/2)

    def test_div_pos_neg(self):
        self.assertEqual(self.calculator.division(1, -2), -1/2)

    def test_div_neg_neg(self):
        self.assertEqual(self.calculator.division(-1, -2), 1/2)

    def test_div_pos_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_div_pos_none(self):
        self.assertRaises(TypeError, self.calculator.division, 1, None)

    def test_div_pos_string(self):
        self.assertRaises(TypeError, self.calculator.division, 1, 'a')

class TestCalculatorAbs(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_abs_neg(self):
        self.assertEqual(self.calculator.absolute(-1), 1)

    def test_abs_pos(self):
        self.assertEqual(self.calculator.absolute(1), 1)

    def test_abs_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_abs_string(self):
        self.assertRaises(TypeError, self.calculator.absolute, '-a')

class TestCalculatorDegree(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_deg_pos(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_deg_neg_odd(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_deg_neg_even(self):
        self.assertEqual(self.calculator.degree(-2, 4), 16)

    def test_deg_string(self):
        self.assertRaises(TypeError, self.calculator.degree, 'a', 2)

    def test_deg_none(self):
        self.assertRaises(TypeError, self.calculator.degree, 1, None)

class TestCalculatorLn(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_ln_pos(self):
        self.assertEqual(self.calculator.ln(1), math.log(1))

    def test_ln_neg(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_string(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

class TestCalculatorLog(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_log_pos_pos(self):
        self.assertEqual(self.calculator.log(2,3), math.log(2,3))

    def test_log_pos_neg(self):
        self.assertRaises(ValueError, self.calculator.log, 2, -2)

    def test_log_neg_pos(self):
        self.assertRaises(ValueError, self.calculator.log, -2, 2)

    def test_log_base_one(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 4, 1)

    def test_log_string(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 'a')

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

class TestCalculatorSqrt(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sqrt_pos(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_neg(self):
        self.assertEqual(self.calculator.sqrt(-4), (-4) ** 0.5)

    def test_sqrt_string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

class TestCalculator_nth_root(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_nth_root_pos(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)

    def test_nth_root_neg(self):
        self.assertEqual(self.calculator.nth_root(-8, 3), (-8) ** (1. / 3))

    def test_nth_root_zero(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 2, 0)

    def test_nth_root_string(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 2)

    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 1, None)

if __name__ == "__main__":
    unittest.main()
