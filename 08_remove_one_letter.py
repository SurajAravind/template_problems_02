# pylint: disable=invalid-name
"""
Remove one letter
Given two strings s0 and s1, return whether you can obtain
s1 by removing 1 letter from s0.

Example 1
Input
s0 = "hello"
s1 = "hello"

Output
False

Example 2
Input
s0 = "hello"
s1 = "helo"

Output
True
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def remove_one_letter(s0, s1):
    pass


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestLargest(unittest.TestCase):

    def test_01(self):
        self.assertEqual(remove_one_letter("hello", "hello"), False)

    def test_02(self):
        self.assertEqual(remove_one_letter("hello", "helo"), True)

    def test_03(self):
        self.assertEqual(remove_one_letter("hello", "hell"), True)

    def test_04(self):
        self.assertEqual(remove_one_letter("a", ""), True)

    def test_05(self):
        self.assertEqual(remove_one_letter("je", "e"), True)

    def test_06(self):
        self.assertEqual(remove_one_letter(
            "coding_culture", "codingculture"), True)

    def test_07(self):
        self.assertEqual(remove_one_letter(
            "pascals_triangle", "pascals triangle"), False)

    def test_08(self):
        self.assertEqual(remove_one_letter(
            "remove_one_letter", "remve_one_letter"), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
