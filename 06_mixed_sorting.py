# pylint: disable=invalid-name
"""
Mixed sorting
Given a list of integers nums, sort the array such that:

All even numbers are sorted in increasing order
All odd numbers are sorted in decreasing order

The relative positions of the even and odd numbers remain the same

Example 1
Input
nums = [8, 13, 11, 90, -5, 4]

Output
[4, 13, 11, 8, -5, 90]

Explanation
The even numbers are sorted in increasing order, the odd numbers
are sorted in decreasing number, and the relative positions were
[even, odd, odd, even, odd, even] and remain the same after sorting.
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def mixed_sorting(nums):
    pass


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,bad-continuation,line-too-long
class TestMixedSorting(unittest.TestCase):

    def test_01(self):
        self.assertEqual(mixed_sorting(
            [8, 13, 11, 90, -5, 4]), [4, 13, 11, 8, -5, 90])

    def test_02(self):
        self.assertEqual(mixed_sorting([]), [])

    def test_03(self):
        self.assertEqual(mixed_sorting([1, 3, 5]), [5, 3, 1])

    def test_04(self):
        self.assertEqual(mixed_sorting([2, 4, 8]), [2, 4, 8])

    def test_05(self):
        self.assertEqual(mixed_sorting([-30, 10, 50]), [-30, 10, 50])

    def test_06(self):
        self.assertEqual(mixed_sorting([1]), [1])

    def test_07(self):
        self.assertEqual(mixed_sorting([2]), [2])

    def test_08(self):
        self.assertEqual(mixed_sorting(
            [16, 98, 24, 35, 4, 79, 93, 39, 11, 76]),
            [4, 16, 24, 93, 76, 79, 39, 35, 11, 98])

    def test_09(self):
        self.assertEqual(mixed_sorting(
            [90, 37, 77, 36, 32, 58, 72, 56, 95, 83, 75, 85, 23, 66, 19, 22]),
            [22, 95, 85, 32, 36, 56, 58, 66, 83, 77, 75, 37, 23, 72, 19, 90])

    def test_10(self):
        self.assertEqual(mixed_sorting(
            [47, 46, 42, 48, 31, 89, 7, 68, 64, 71, 96, 65, 57, 73, 10, 67, 91, 38, 88, 26, 92, 55, 1, 62]),
            [91, 10, 26, 38, 89, 73, 71, 42, 46, 67, 48, 65, 57, 55, 62, 47, 31, 64, 68, 88, 92, 7, 1, 96])


if __name__ == '__main__':
    unittest.main(verbosity=2)
