import unittest
from .solution_inefficient import minimumBribes


class TestMinimumBribes(unittest.TestCase):
    def test_one_bribe(self):
        q = [1, 2, 4, 3]
        number_of_bribes = minimumBribes(q)
        self.assertEqual(number_of_bribes, 1)

    def test_two_single_bribes(self):
        q = [1, 2, 4, 3, 6, 5]
        number_of_bribes = minimumBribes(q)
        self.assertEqual(number_of_bribes, 2)

    def test_bribed_bribes(self):
        q = [1, 4, 3, 2]
        number_of_bribes = minimumBribes(q)
        self.assertEqual(number_of_bribes, 3)

    def test_bribed_bribes_with_other_bribes(self):
        q = [1, 4, 3, 5, 2]
        number_of_bribes = minimumBribes(q)
        self.assertEqual(number_of_bribes, 4)

    def test_chaotic(self):
        q = [4, 1, 2, 3]
        number_of_bribes = minimumBribes(q)
        self.assertEqual(number_of_bribes, "Too chaotic")


if __name__ == "__main__":
    unittest.main()
