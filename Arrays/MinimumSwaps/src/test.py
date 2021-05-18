import unittest
from .solution import minimumSwaps

class TestMinimumSwaps(unittest.TestCase):
    def test_single_swap(self):
        a = [3, 2, 1]
        res = minimumSwaps(a)
        self.assertEqual(res, 1)

    def test_five_swaps(self):
        a = [7, 1, 3, 2, 4, 5, 6]
        res = minimumSwaps(a)
        self.assertEqual(res, 5)

    def test_three_swaps(self):
        a = [4, 3, 1, 2]
        res = minimumSwaps(a)
        self.assertEqual(res, 3)

    def test_three_swaps_v2(self):
        a = [1, 3, 5, 2, 4, 6, 7]
        res = minimumSwaps(a)
        self.assertEqual(res, 3)

    def test_three_swaps_v3(self):
        a = [2, 3, 4, 1, 5]
        res = minimumSwaps(a)
        self.assertEqual(res, 3)

if __name__ == "__main__":
    unittest.main()