####################
# test_calc.py
# By Sidhant Soni
# November 11, 2018
####################

# import statements
import unittest
import calc


class knownvalue(unittest.TestCase):
    # Test Divide
    def test_divide(self):
        # Capture the results of the function
        result = calc.arthDivide(10,5)
        # Check for expected output
        expected = 2.0
        self.assertEqual(expected,result)

    # Test Add
    def test_add(self):
        # Capture the results of the function
        result = calc.add(10,5)
        # Check for expected output
        expected = 15
        self.assertEqual(expected,result)

    # Test Add
    def test_add1(self):
        # Capture the results of the function
        result = calc.add(11,5)
        # Check for expected output
        expected = 16
        self.assertEqual(expected,result)

    # Test Add
    def test_add2(self):
        # Capture the results of the function
        result = calc.add(12,5)
        # Check for expected output
        expected = 17
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()

