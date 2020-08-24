# pylint: disable=invalid-name
"""
Flatten Lists
Given a list of list of integers, flatten the elements into
a single list and return it.

Example 1
Input

lsts = [[1, 2], [3, 4, 5]]
Output

[1, 2, 3, 4, 5]
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput

# See if you can use chain from itertools (https://docs.python.org/3/library/itertools.html)
# import itertools


def flatten_list(lsts):
    pass


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestFlattenList(unittest.TestCase):

    def test_01(self):
        self.assertEqual(flatten_list([[1, 2], [3, 4, 5]]), [1, 2, 3, 4, 5])

    def test_02(self):
        self.assertEqual(flatten_list([[1]]), [1])

    def test_03(self):
        self.assertEqual(flatten_list([]), [])

    def test_04(self):
        self.assertEqual(flatten_list([[1, 2], [89], [13, 44, 59]]),
                         [1, 2, 89, 13, 44, 59])

    def test_05(self):
        self.assertEqual(flatten_list([[], [3, 4, 5]]), [3, 4, 5])

    def test_06(self):
        self.assertEqual(flatten_list(
            [[1, 2], [], [], [], [3], [4, 5]]), [1, 2, 3, 4, 5])

    def test_07(self):
        self.assertEqual(flatten_list(
            [[1], [2], [3], [4], [5]]), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main(verbosity=2)
