# pylint: disable=invalid-name
"""
Pascal's triangle
Given an integer n, return the nth (0-indexed) row of Pascal's triangle.

Pascal's triangle can be created as follows: In the top row, there is
an array of 1. Subsequent row is created by adding the number above and
to the left with the number above and to the right, treating empty elements as 0.

The first few rows are:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Example 1
Input
n = 3

Output
[1, 3, 3, 1]

Explanation
This is row 3 in
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def pascals_triangle(n):
    pass


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestPascalsTriangle(unittest.TestCase):

    def test_01(self):
        self.assertEqual(pascals_triangle(3), [1, 3, 3, 1])

    def test_02(self):
        self.assertEqual(pascals_triangle(0), [1])

    def test_03(self):
        self.assertEqual(pascals_triangle(1), [1, 1])

    def test_04(self):
        self.assertEqual(pascals_triangle(2), [1, 2, 1])

    def test_05(self):
        self.assertEqual(pascals_triangle(7), [1, 7, 21, 35, 35, 21, 7, 1])

    def test_06(self):
        self.assertEqual(pascals_triangle(12),
                         [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1])

    def test_07(self):
        self.assertEqual(pascals_triangle(19),
                         [1, 19, 171, 969, 3876, 11628, 27132, 50388, 75582, 92378, 92378, 75582, 50388, 27132, 11628, 3876, 969, 171, 19, 1])

    def test_08(self):
        self.assertEqual(pascals_triangle(23), [1, 23, 253, 1771, 8855, 33649, 100947, 245157, 490314, 817190,
                                                1144066, 1352078, 1352078, 1144066, 817190, 490314, 245157, 100947, 33649, 8855, 1771, 253, 23, 1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
