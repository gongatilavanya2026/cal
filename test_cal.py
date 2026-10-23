import unittest
from cal import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()