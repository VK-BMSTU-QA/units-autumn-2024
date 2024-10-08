import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # сложение
    # сложение int
    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    # сложение отрицательного и положительного чисел
    def test_add_negative_and_positive(self):
        self.assertEqual(self.calculator.addition(-1, 1), 0)

    # сложение отрицательных чисел
    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-2, -4), -6)

    # сложение нуля и числа
    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(0, 5), 5)

    # сложение бесконечности
    def test_add_inf_positive(self):
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
    
    def test_add_inf_negative(self):
        self.assertEqual(self.calculator.addition(-math.inf, -1), -math.inf)

    # сложение float
    def test_add_float(self):
        self.assertEqual(self.calculator.addition(1.2, 2.3), 3.5)

    # сложение строки и числа
    def test_add_str(self):
        self.assertRaises(TypeError, self.calculator.addition, 'abc', 4)

    # сложение None
    def test_add_None(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    # сложение больших чисел
    def test_add_big(self):
        self.assertEqual(self.calculator.addition(10**100, 10**100), 2 * 10**100)

    # сложение float и int
    def test_add_float_int(self):
        self.assertEqual(self.calculator.addition(1.5, 2), 3.5)

    # комплексное сложение
    def test_addition_complex(self):
        self.assertEqual(self.calculator.addition(complex(1, 2), complex(3, 4)), complex(4, 6))


    # умножение
    # умножение int
    def test_mul_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    # умножение отрицательного и положительного числа
    def test_mul_negative_and_positive(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    # умножение отрицательных чисел
    def test_mul_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -4), 8)

    # умножение нуля и числа
    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 3), 0)

    # умножение бесконечности
    def test_mul_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, -1), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, 1), -math.inf)

    # умножение float
    def test_mul_float(self):
        self.assertEqual(self.calculator.multiplication(1.2, 2.3), 2.76)

    # умножение строки и числа
    def test_mul_str(self):
        self.assertEqual(self.calculator.multiplication('2', 3), '222')

    # умножение строк
    def test_mul_str_str(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'abc', 'xyz')
    
    # умножение None
    def test_mul_None(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)
    
    # умножение больших чисел
    def test_mul_big(self):
        self.assertEqual(self.calculator.multiplication(10**100, 10**100), 10**200)

    # умножение нуля на ноль
    def test_mul_zero_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    # умножение float на int
    def test_mul_float_int(self):
        self.assertEqual(self.calculator.multiplication(1.5, 2), 3.0)

    # комплексное умножение
    def test_multiplication_complex(self):
        self.assertEqual(self.calculator.multiplication(complex(1, 2), complex(3, 4)), complex(-5, 10))


    # вычитание
    # вычитание int
    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    # вычитание отрицательного и положительного числа
    def test_sub_negative_and_positive(self):
        self.assertEqual(self.calculator.subtraction(-3, 2), -5)

    # вычитание отрицательных чисел
    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(-3, -2), -1)

    # вычитание нуля и числа
    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(3, 0), 3)

    # вычитание бесконечности
    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, -1), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 1), -math.inf)

    # вычитание float
    def test_sub_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.3, 1.2), 1.1, places=7)

    # вычитание строки и числа
    def test_sub_str(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'abc', 4)

    # вычитание строк
    def test_sub_str_str(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'abc', 'xyz')

    # вычитание None
    def test_sub_None(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    # вычитание больших чисел
    def test_sub_big(self):
        self.assertEqual(self.calculator.subtraction(10**100, 10**101), -9 * 10**100)

    # вычитание нуля из нуля
    def test_sub_zero_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    # комплексное вычитание
    def test_subtraction_complex(self):
        self.assertEqual(self.calculator.subtraction(complex(1, 2), complex(3, 4)), complex(-2, -2))

    
    # деление
    # деление int
    def test_div_int(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    # деление отрицательного и положительного числа
    def test_div_negative_and_positive(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)

    # деление отрицательных чисел
    def test_div_negative(self):
        self.assertEqual(self.calculator.division(-6, -2), 3)

    # деление нуля и числа
    def test_div_zero(self):
        self.assertEqual(self.calculator.division(0, 3), 0)

    # деление бесконечности
    def test_div_inf(self):
        self.assertEqual(self.calculator.division(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, -1), math.inf)
        self.assertEqual(self.calculator.division(math.inf, -1), -math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 1), -math.inf)

    # деление float
    def test_div_float(self):
        self.assertAlmostEqual(self.calculator.division(2.3, 1.2), 1.9166666666666667, places=7)

    # деление строки и числа
    def test_div_str(self):
        self.assertRaises(TypeError, self.calculator.division, 'abc', 4)

    # деление строк
    def test_div_str_str(self):
        self.assertRaises(TypeError, self.calculator.division, 'abc', 'xyz')

    # деление None
    def test_div_None(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    # деление больших чисел
    def test_div_big(self):
        self.assertAlmostEqual(self.calculator.division(10**100, 10**99), 10.0, places=7)

    # деление на ноль
    def test_div_zero_zero(self):
        self.assertIsNone(self.calculator.division(1, 0))

    # комплексное деление
    def test_division_complex(self):
        self.assertAlmostEqual(self.calculator.division(complex(1, 2), complex(3, 4)), complex(0.44, 0.08), places=7)

    # модуль
    # модуль int
    def test_absolute_int(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    # модуль отрицательного числа
    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    # модуль нуля
    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    # модуль бесконечности
    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    # модуль строки
    def test_absolute_str(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'abc')

    # модуль None
    def test_absolute_None(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    # модуль отрицательного числа близкого к нулю
    def test_absolute_negative_zero(self):
        self.assertEqual(self.calculator.absolute(-1e-15), 1e-15)

    # комплексный модуль
    def test_absolute_complex(self):
        self.assertAlmostEqual(self.calculator.absolute(complex(3, 4)), 5.0)

    
    # степень
    # степень int
    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    # степень отрицательного числа с float
    def test_degree_negative_float(self):
        self.assertAlmostEqual(self.calculator.degree(-2.0, 3), -8.0)

    # степень отрицательного числа
    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    # степень нуля
    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    # степень отрицательной степени
    def test_degree_negative_degree(self):
        self.assertEqual(self.calculator.degree(2, -1), 0.5)

    # степень единицы
    def test_degree_one(self):
        self.assertEqual(self.calculator.degree(2, 1), 2)

    # степень бесконечности
    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 2), math.inf)

    # степень строки
    def test_degree_str(self):
        self.assertRaises(TypeError, self.calculator.degree, 'abc', 2)

    # строка-степень
    def test_degree_str_degree(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, 'abc')

    # None-степень
    def test_degree_None_degree(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    # степень-None
    def test_degree_degree_None(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)

    # степень нуля в нулевой степени
    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    # степень большого числа
    def test_degree_big(self):
        self.assertAlmostEqual(self.calculator.degree(10**6, 3), 10**18)

    # комплексная степень
    def test_degree_complex(self):
        self.assertAlmostEqual(self.calculator.degree(complex(1, 2), 3), complex(-11, -2), places=7)


    # натуральный логарифм
    # ln от e
    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    # ln от 1
    def test_ln_one(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    # ln от бесконечности
    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    # ln от нуля
    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    # ln от отрицательного числа
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    # ln от строки
    def test_ln_str(self):
        self.assertRaises(TypeError, self.calculator.ln, 'abc')

    # ln от None
    def test_ln_None(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    # ln от числа близкого к нулю
    def test_ln_zero_near(self):
        self.assertAlmostEqual(self.calculator.ln(1e-100), -230.25850929940458)

    # комплексный ln
    def test_ln_complex(self):
        self.assertRaises(TypeError, self.calculator.ln, 1 + 2j)


    # логарифм
    # log от int по основанию int
    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3)

    # log от 1 по основанию 10
    def test_log_one(self):
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)

     # log от float по основанию 10
    def test_log_one_float(self):
        self.assertAlmostEqual(self.calculator.log(1.0, 10), 0.0)

    # log от бесконечности
    def test_log_inf(self):
        self.assertEqual(self.calculator.log(math.inf, 10), math.inf)

    # log от нуля
    def test_log_zero(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 10)

    # log от отрицательного числа
    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -1, 10)

    # log от числа по основанию 1
    def test_log_one_degree(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 8, 1)

    # log от числа по отрицательному основанию
    def test_log_negative_degree(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -1)

    # log от числа по нулевому основанию
    def test_log_zero_degree(self):
        self.assertRaises(ValueError, self.calculator.log, 8, 0)

    # log от строки
    def test_log_str(self):
        self.assertRaises(TypeError, self.calculator.log, 'abc', 2)

    # log от числа по строковому основанию
    def test_log_str_degree(self):
        self.assertRaises(TypeError, self.calculator.log, 8, 'abc')

    # log от None
    def test_log_None(self):
        self.assertRaises(TypeError, self.calculator.log, None, 2)

    # log от числа по None-основанию
    def test_log_None_degree(self):
        self.assertRaises(TypeError, self.calculator.log, 8, None)

    # log от большого числа
    def test_log_big(self):
        self.assertAlmostEqual(self.calculator.log(10**100, 10), 100, places=7)

    # комплексный log
    def test_log_complex(self):
        self.assertRaises(TypeError, self.calculator.log, 1 + 2j)
    
    # квадратный корень
    # sqrt от int
    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2)
    
     # sqrt от float
    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(4.0), 2.0)

    # sqrt от нуля
    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    # sqrt от бесконечности
    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    # sqrt от отрицательного числа
    def test_sqrt_negative(self):
         self.assertAlmostEqual(self.calculator.sqrt(-1), 1j)

    # sqrt от строки
    def test_sqrt_str(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'abc')

    # sqrt от None
    def test_sqrt_None(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    # sqrt от большого числа
    def test_sqrt_big(self):
        self.assertAlmostEqual(self.calculator.sqrt(10**100), 10**50, places=7)

    # комплексный sqrt
    def test_sqrt_complex(self):
        self.assertAlmostEqual(self.calculator.sqrt(complex(1, 2)), complex(1.272019649514069, 0.7861513777574233), places=7)

    
    #  n-ный корень
    # nth_root от int по int нечетной/четной степени
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)
        self.assertAlmostEqual(self.calculator.nth_root(16, 4), 2)

    # nth_root от float по int степени
    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(27.0, 3), 3.0)


    # nth_root от бесконечности
    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.nth_root(-math.inf, 2), math.inf)

    # nth_root от отрицательного числа
    def test_nth_root_negative(self):
        self.assertTrue(self.calculator.nth_root(-27, 3).imag != 0)

    # nth_root с нулевой степенью
    def test_nth_root_zero_degree(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 27, 0)

    # nth_root от строки
    def test_nth_root_str(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'abc', 2)

    # nth_root от числа по строковой степени
    def test_nth_root_str_degree(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 27, 'abc')

    # nth_root от None
    def test_nth_root_None(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, 2)

    # nth_root от числа по None-степени
    def test_nth_root_None_degree(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 27, None)

    # nth_root от большого числа
    def test_nth_root_big(self):
        self.assertAlmostEqual(self.calculator.nth_root(10**30, 10), 10**3, places=7)

    # комплексный nth_root
    def test_nth_root_complex(self):
        self.assertAlmostEqual(self.calculator.nth_root(complex(1, 2), 3), complex(1.2196165079717578, 0.47171126778938893), places=7)


if __name__ == "__main__":
    unittest.main()
