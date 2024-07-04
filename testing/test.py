import sys
import os
import unittest
from fractions import Fraction

# Specify the directory name directly if the script is always in 'testing'
current_dir = 'testing'

# Get the path to the 'calculator' directory relative to 'testing'
calculator_dir = os.path.abspath(os.path.join(current_dir, '..', 'calculator'))

# Add 'calculator' directory to the sys.path
sys.path.append(calculator_dir)

# Import the sum function from my_sum module in 'calculator'
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))  # Adjusted expected result

    def test_bad_type(self):
        """
        Test that it raises TypeError for non-iterable input
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()



