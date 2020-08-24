# pylint: disable=invalid-name
"""
Shortest sublist to sort list
Given a list of integers nums, return the length of the
shortest sublist in nums which if sorted would make nums
sorted in ascending order.

Example 1
Input
nums = [0, 1, 4, 3, 8, 9]

Output
2

Explanation
Sorting the sublist [4, 3] would get us [0, 1, 3, 4, 8, 9]

Example 2
Input
nums = [5, 4, 3, 2, 8, 9]

Output
4

Explanation
Sorting the sublist [5, 4, 3, 2] would get us [2, 3, 4, 5, 8, 9]

Example 3
Input
nums = [1, 2, 3, 5, 9, 8, 5]

Output
3

Explanation
Sorting the sublist [9, 8, 5] would get us [1, 2, 3, 5, 5, 8, 9]
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def shortlist(nums):
    pass


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable,line-too-long
class TestShortlist(unittest.TestCase):

    def test_01(self):
        self.assertEqual(shortlist([0, 1, 4, 3, 8, 9]), 2)

    def test_02(self):
        self.assertEqual(shortlist([5, 4, 3, 2, 8, 9]), 4)

    def test_03(self):
        self.assertEqual(shortlist([1, 2, 3, 5, 9, 8, 5]), 3)

    def test_04(self):
        self.assertEqual(shortlist([6, 7, 8, 1, 4]), 5)

    def test_05(self):
        self.assertEqual(
            shortlist([1, 2, 10, 3, 4, 7]), 4)

    def test_06(self):
        self.assertEqual(
            shortlist([48, 49, 54, 55, 66, 67, 93, 95, 97, 20, 22, 28, 28, 36, 45]), 15)

    def test_07(self):
        self.assertEqual(shortlist([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                                    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), 0)

    def test_08(self):
        self.assertEqual(shortlist([
            11, 16, 29, 30, 31, 33, 33, 33, 256, 260, 263, 265, 265, 266, 269, 271, 275, 278, 278, 280, 285, 293, 298, 300, 300, 302, 312, 313, 316, 318, 324, 332, 333, 335, 336, 43, 45, 52, 55, 57, 59, 71, 72, 79, 79, 79, 85, 87, 89, 94, 98, 100, 102, 103, 104, 110, 112, 116, 118, 121, 122, 124, 133, 133, 134, 136, 147, 153, 157, 159, 161, 167, 177, 179, 182, 182, 183, 189, 199, 202, 202, 216, 216, 217, 218, 223, 227, 228, 228, 243, 254, 255, 255, 336, 337, 341]), 85)


if __name__ == '__main__':
    unittest.main(verbosity=2)
