import unittest
from src.coverage_foo import MyClass
import math


class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.my_class = MyClass()

    def test_my_class_positive(self):
        self.assertEqual(self.my_class.my_foo(3, 4), 5)

    def test_my_class_positive_1(self):
        self.assertEqual(self.my_class.my_foo(1, 1), 2)

    def test_my_class_positive_2(self):
        self.assertEqual(self.my_class.my_foo(-10, 12), 2)

    def test_my_class_positive_3(self):
        self.assertEqual(self.my_class.my_foo(-10, -1232), -1242)

    def test_my_class_positive_4(self):
        self.assertEqual(self.my_class.my_foo(0, 0), 0)

    def test_my_class_positive_5(self):
        self.assertLess(self.my_class.my_foo(-1, 1.1), 0.11)

    def test_my_class_positive_6(self):
        self.assertEqual(self.my_class.my_foo(0.123, -0.123), 0)

    def test_my_class_positive_7(self):
        self.assertEqual(self.my_class.my_foo(3, 12), 16)

    def test_my_class_positive_8(self):
        self.assertEqual(self.my_class.my_foo(-10, 4), -10.4)

    def test_my_class_positive_9(self):
        self.assertEqual(self.my_class.my_foo(3, 0), 4)

    def test_my_class_positive_10(self):
        self.assertEqual(self.my_class.my_foo(math.inf, math.inf), math.inf)

    def test_my_class_positive_11(self):
        self.assertEqual(self.my_class.my_foo(-math.inf, -math.inf), -math.inf)

    def test_my_class_positive_12(self):
        self.assertTrue(math.isnan(self.my_class.my_foo(math.inf, -math.inf)))

    def test_my_class_positive_13(self):
        self.assertEqual(self.my_class.my_foo(math.inf, 4), math.inf)

    def test_my_class_positive_14(self):
        self.assertEqual(self.my_class.my_foo(1.2, 2.3000000001), 3.5000000001)

    def test_my_class_positive_15(self):
        self.assertEqual(self.my_class.my_foo(1.2, 2.3), 3.5)

    def test_my_class_negative(self):
        self.assertRaises(ZeroDivisionError, self.my_class.my_foo, 0, 4)

    def test_my_class_negative_1(self):
        self.assertRaises(TypeError, self.my_class.my_foo, None, None)

    def test_my_class_negative_2(self):
        self.assertRaises(TypeError, self.my_class.my_foo, {2, 3}, 123)

    def test_my_class_negative_3(self):
        self.assertRaises(TypeError, self.my_class.my_foo, [2, 3, 4], 'Goida')

    def test_my_class_negative_4(self):
        self.assertRaises(TypeError, self.my_class.my_foo, dict(), {123123, 3})

    def test_my_class_negative_5(self):
        self.assertRaises(TypeError, self.my_class.my_foo, 'abc', 4)


if __name__ == "__main__":
    unittest.main()
