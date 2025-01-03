import unittest

# Function to calculate the sum of two numbers
def add_numbers(a, b):
    return a + b

# Unit test class
class TestAddNumbers(unittest.TestCase):

    # Test case 1: Test with positive numbers
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(5, 7), 12)

    # Test case 2: Test with negative numbers
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -7), -12)

    # Test case 3: Test with a positive and a negative number
    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(5, -3), 2)

    # Test case 4: Test with zero
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, 5), 5)

if __name__ == '__main__':
    unittest.main()
