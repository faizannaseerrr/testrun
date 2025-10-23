import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add("a", 3), "Error: Invalid input")

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertEqual(self.calc.subtract("a", 3), "Error: Invalid input")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply("a", 3), "Error: Invalid input")

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by zero")
        self.assertEqual(self.calc.divide("a", 3), "Error: Invalid input")

    def test_memory_functions(self):
        self.assertEqual(self.calc.store_in_memory(15), "Stored 15 in memory")
        self.assertEqual(self.calc.recall_memory(), 15)
        self.assertEqual(self.calc.clear_memory(), "Memory cleared")
        self.assertEqual(self.calc.recall_memory(), 0)
        self.assertEqual(self.calc.store_in_memory("a"), "Error: Invalid input")

    def test_variable_assignment(self):
        self.assertEqual(self.calc.assign_variable("x", 5), "Assigned x = 5")
        self.assertEqual(self.calc.assign_variable("y", 10), "Assigned y = 10")
        self.assertEqual(self.calc.assign_variable("123", 5), "Error: Invalid variable name")
        self.assertEqual(self.calc.assign_variable("x", "a"), "Error: Invalid value")

    def test_evaluate_expression(self):
        self.calc.assign_variable("x", 5)
        self.calc.assign_variable("y", 2)
        self.assertEqual(self.calc.evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(self.calc.evaluate_expression("(2 + 3) * 4"), 20)
        self.assertEqual(self.calc.evaluate_expression("x * y + 3"), 13)
        self.assertEqual(self.calc.evaluate_expression("x / 0"), "Error: Division by zero")
        self.assertEqual(self.calc.evaluate_expression("x + z"), "Error: Invalid expression")  # z not defined
        self.assertEqual(self.calc.evaluate_expression("x ++ 5"), "Error: Invalid expression")

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(9), 3.0)
        self.assertEqual(self.calc.sqrt(0), 0.0)
        self.assertEqual(self.calc.sqrt(-4), "Error: Cannot take square root of negative number")
        self.assertEqual(self.calc.sqrt("a"), "Error: Invalid input")

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power("a", 3), "Error: Invalid input")

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(-5), "Error: Factorial of negative number is undefined")
        self.assertEqual(self.calc.factorial(3.5), "Error: Invalid input")
        self.assertEqual(self.calc.factorial(1001), "Error: Number too large")

if __name__ == '__main__':
    unittest.main()