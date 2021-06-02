import unittest
from .solution import Solution


class TwoSumTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one(self):
        nums, target = [3, 4, 3], 6
        res = self.sol.twoSum(nums, target)
        self.assertListEqual(res, [0, 2])

    def test_two(self):
        nums = [3, 3]
        target = 6
        res = self.sol.twoSum(nums, target)
        self.assertListEqual(res, [0, 1])

    def test_three(self):
        nums = [2, 7, 11, 15]
        target = 9
        res = self.sol.twoSum(nums, target)
        self.assertListEqual(res, [0, 1])


if __name__ == '__main__':
    unittest.main()
