import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(2, 2), 4)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(0, 0), 0)

        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.addition(1.2, 2.3), 3.5)
        self.assertEqual(self.calculator.addition(1.2, 2), 3.2)
        self.assertEqual(self.calculator.addition(1.2, 0), 1.2)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-1, -1.2), -2.2)
        self.assertEqual(self.calculator.addition(-1, 0), -1)
        self.assertEqual(self.calculator.addition(-1, 1), 0)

        # Тесты с бесконечностью
        self.assertTrue(not math.isnan(self.calculator.multiplication(math.inf, -math.inf)))
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, -1), math.inf)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.addition(2, [1, 2])
            self.calculator.addition("a", [1, 2])
            self.calculator.addition("hello", 1)

    def test_multiply(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(2, 2), 4)
        self.assertEqual(self.calculator.multiplication(1.2, 2), 2.4)
        self.assertEqual(self.calculator.multiplication(1.2, 2.3), 2.76)

        # Тесты с нулем
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        self.assertEqual(self.calculator.multiplication(-1, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)
        self.assertEqual(self.calculator.multiplication(-1.2, 2), -2.4)
        self.assertEqual(self.calculator.multiplication(-1.2, -2.3), 2.76)

        # Тесты с бесконечностью
        self.assertTrue(math.isnan((self.calculator.multiplication(math.inf, 0))))
        self.assertEqual(self.calculator.multiplication(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, math.inf), -math.inf)

        # Тест на исключения
        with self.assertRaises(TypeError):
            self.calculator.multiplication(2, [1, 2])
            self.calculator.multiplication("a", [1, 2])
            self.calculator.multiplication("hello", 1)
            self.calculator.multiplication("hello", "world")

    def test_subtract(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.subtraction(2.6, 1.1), 1.5)
        self.assertEqual(self.calculator.subtraction(2.0, 1.2), 0.8)
        self.assertEqual(self.calculator.subtraction(1.2, 0), 1.2)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
        self.assertEqual(self.calculator.subtraction(-2.6, -1.3), -1.3)
        self.assertEqual(self.calculator.subtraction(-1, 0), -1)
        self.assertEqual(self.calculator.subtraction(-1, 1), -2)

        # Тесты с бесконечностью
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))
        self.assertEqual(self.calculator.subtraction(math.inf, -math.inf), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, math.inf), -math.inf)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, [1, 2])
            self.calculator.subtraction("a", 1)
            self.calculator.subtraction("hello", [1, 2])

    def test_division(self):
        # Тесты с целыми числами
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(0, 1), 0)

        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.division(5.5, 2), 2.75)
        self.assertEqual(self.calculator.division(7.2, 3.6), 2.0)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.division(-6, 2), -3)
        self.assertEqual(self.calculator.division(-5, -2), 2.5)
        self.assertEqual(self.calculator.division(6, -3), -2)

        # Тесты с бесконечностью
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))
        self.assertEqual(self.calculator.division(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, -2), math.inf)

        # Тесты на исключение при делении на ноль
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertEqual(self.calculator.division(0, 0), None)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.division(2, [1, 2])
            self.calculator.division("a", 1)
            self.calculator.division("hello", [1, 2])

    def test_absolute(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(1.23), 1.23)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(-1.23), 1.23)

        # Тесты с нулем
        self.assertEqual(self.calculator.absolute(0), 0)

        # Тесты с бесконечностью
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.absolute([1, 2])
            self.calculator.absolute("a")
            self.calculator.absolute("hello")

    def test_degree(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 2), 25)
        self.assertEqual(self.calculator.degree(10, 1), 10)
        self.assertEqual(self.calculator.degree(7, 0), 1)

        # Тесты с отрицательными числами
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertEqual(self.calculator.degree(-5, 1), -5)
        self.assertEqual(self.calculator.degree(-5, 0), 1)

        # Тесты с числами с плавающей точкой
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)
        self.assertEqual(self.calculator.degree(9, 0.5), 3)

        # Тесты с бесконечностью
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, -1), 0)
        self.assertEqual(self.calculator.degree(1, math.inf), 1)
        self.assertEqual(self.calculator.degree(0, math.inf), 0)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.degree(2, [1, 2])
            self.calculator.degree("a", 2)
            self.calculator.degree(2, "b")

    def test_ln(self):
        # Тесты с положительными числами
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(10), 2.302585, places=6)

        # Тесты с числами с плавающей точкой
        self.assertAlmostEqual(self.calculator.ln(2.71828), 0.999999, places=6)

        # Тесты с бесконечностью
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        # Тесты на исключения
        with self.assertRaises(ValueError):
            self.calculator.ln(0)
            self.calculator.ln(-1)

        # Тесты на исключения при неправильных типах данных
        with self.assertRaises(TypeError):
            self.calculator.ln("a")
            self.calculator.ln([1, 2])

    def test_log(self):
        self.assertEqual(self.calculator.log(1, 10), 0)
        self.assertEqual(self.calculator.log(10, 10), 1)
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertAlmostEqual(self.calculator.log(100, 10), 2, places=6)

        self.assertAlmostEqual(self.calculator.log(2.71828, math.e), 1, places=5)
        self.assertAlmostEqual(self.calculator.log(5.5, 2), 2.459432, places=6)

        self.assertEqual(self.calculator.log(math.inf, 10), math.inf)

        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)
            self.calculator.log(-1, 10)
            self.calculator.log(10, -2)
            self.calculator.log(10, 1)
            self.calculator.log(10, 0)

        with self.assertRaises(TypeError):
            self.calculator.log("a", 10)
            self.calculator.log(10, "b")
            self.calculator.log([1, 2], 10)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(2), 1.414214, places=6)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(1), 1)

        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

        self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)
        self.assertAlmostEqual(self.calculator.sqrt(4.5), 2.12132034)

        with self.assertRaises(TypeError):
            self.calculator.sqrt("a")
            self.calculator.sqrt([1, 2])

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertAlmostEqual(self.calculator.nth_root(81, 4), 3, places=6)
        self.assertAlmostEqual(self.calculator.nth_root(2, 2), 1.414214, places=6)
        self.assertEqual(self.calculator.nth_root(0, 5), 0)
        self.assertEqual(self.calculator.nth_root(1, 10), 1)

        self.assertAlmostEqual(self.calculator.nth_root(27.5, 4), 2.2899878)
        self.assertAlmostEqual(self.calculator.nth_root(27, 4.5), 2.0800838)

        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)

        self.calculator.nth_root(-1, 2)
        self.calculator.nth_root(1, -2)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(1, 0)

        with self.assertRaises(TypeError):
            self.calculator.nth_root("a", 2)
            self.calculator.nth_root(2, "b")
            self.calculator.nth_root([1, 2], 2)


if __name__ == "__main__":
    unittest.main()
