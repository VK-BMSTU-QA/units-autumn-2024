import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add1(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add2(self):
        self.assertEqual(self.calculator.addition(-1, 1), 0)

    def test_add3(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add4(self):
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, 1)))

    def test_add5(self):
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, 1)))

    def test_subtract1(self):
        self.assertEqual(self.calculator.subtraction(10, 5), 5)

    def test_subtract2(self):
        self.assertEqual(self.calculator.subtraction(0, 5), -5)

    def test_subtract3(self):
        self.assertEqual(self.calculator.subtraction(-5, -5), 0)

    def test_subtract4(self):
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, 1)))

    def test_subtract5(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 1)))

    def test_multiply1(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)

    def test_multiply2(self):
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)

    def test_multiply3(self):
        self.assertEqual(self.calculator.multiplication(0, 100), 0)

    def test_multiply4(self):
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, 1)))

    def test_multiply5(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 1)))

    def test_divide(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_divide1(self):
        self.assertEqual(self.calculator.division(5, 1), 5)

    def test_divide2(self):
        self.assertEqual(self.calculator.division(0, 1), 0)

    def test_divide3(self):
        self.assertIsNone(self.calculator.division(5, 0))

    def test_divide4(self):
        self.assertTrue(math.isinf(self.calculator.division(math.inf, 1)))

    def test_divide5(self):
        self.assertTrue(math.isnan(self.calculator.division(1, math.nan)))

    def test_absolute1(self):
        self.assertEqual(self.calculator.absolute(-10), 10)

    def test_absolute2(self):
        self.assertEqual(self.calculator.absolute(10), 10)

    def test_absolute3(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute4(self):
        self.assertTrue(math.isinf(self.calculator.absolute(math.inf)))

    def test_absolute5(self):
        self.assertTrue(math.isnan(self.calculator.absolute(math.nan)))

    def test_degree1(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree2(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree3(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree4(self):
        self.assertTrue(math.isinf(self.calculator.degree(math.inf, 2)))

    def test_degree5(self):
        self.assertTrue(math.isnan(self.calculator.degree(math.nan, 2)))

    def test_ln1(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln2(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln3(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln4(self):
        self.assertTrue(math.isinf(self.calculator.ln(math.inf)))

    def test_ln5(self):
        self.assertTrue(math.isnan(self.calculator.ln(math.nan)))

    def test_log1(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log2(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    def test_log3(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 10)

    def test_log4(self):
        self.assertTrue(math.isinf(self.calculator.log(math.inf, 10)))

    def test_log5(self):
        self.assertTrue(math.isnan(self.calculator.log(math.nan, 10)))

    def test_sqrt1(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_sqrt2(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt3(self):
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))

    def test_sqrt4(self):
        self.assertTrue(math.isinf(self.calculator.sqrt(math.inf)))

    def test_sqrt5(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))

    def test_nth_root1(self):
        self.assertAlmostEqual(self.calculator.nth_root(125, 3), 5)

    def test_nth_root2(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

    def test_nth_root3(self):
        self.assertTrue(math.isinf(self.calculator.nth_root(math.inf, 3)))

    def test_nth_root4(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(math.nan, 3)))


if __name__ == "__main__":
    unittest.main()
