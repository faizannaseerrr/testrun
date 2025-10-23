import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertIn("Error", self.calc.add("a", 3))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(3.5, 1.2), 2.3)
        self.assertIn("Error", self.calc.subtract(None, 3))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10)
        self.assertIn("Error", self.calc.multiply([], 3))

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by zero")
        self.assertIn("Error", self.calc.divide("a", 3))

    def test_memory_functions(self):
        self.assertEqual(self.calc.recall_memory(), 0)
        self.assertEqual(self.calc.store_in_memory(15), 15)
        self.assertEqual(self.calc.recall_memory(), 15)
        self.assertEqual(self.calc.clear_memory(), "Memory cleared")
        self.assertEqual(self.calc.recall_memory(), 0)
        self.assertIn("Error", self.calc.store_in_memory("abc"))

    def test_variable_assignment(self):
        self.assertEqual(self.calc.assign_variable("x", 5), "x = 5.0")
        self.assertEqual(self.calc.assign_variable("y", -3.5), "y = -3.5")
        self.assertIn("Error", self.calc.assign_variable("123", 5))
        self.assertIn("Error", self.calc.assign_variable("x", "abc"))

    def test_evaluate_expression(self):
        self.calc.assign_variable("x", 10)
        self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("x * 2"), 20)
        self.assertEqual(self.calc.evaluate_expression("2 * (3 + 4)"), 14)
        self.assertEqual(self.calc.evaluate_expression("10 / 2"), 5)
        self.assertIn("Error", self.calc.evaluate_expression("x / 0"))
        self.assertIn("Error", self.calc.evaluate_expression("x + @"))

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(2.25), 1.5)
        self.assertEqual(self.calc.sqrt(-4), "Error: Cannot take square root of negative number")
        self.assertIn("Error", self.calc.sqrt("a"))

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertIn("Error", self.calc.power("a", 2))

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(-1), "Error: Factorial is not defined for negative numbers")
        self.assertEqual(self.calc.factorial(3.5), "Error: Factorial is only defined for integers")
        self.assertIn("Error", self.calc.factorial("a"))

if __name__ == '__main__':
    unittest.main()