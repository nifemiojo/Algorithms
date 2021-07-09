import unittest
from .solution import solution


class TestBinaryGap(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_test(self):
        res = solution(89)
        self.assertEqual(res, 2)

    def test_second_test(self):
        res = solution(18)
        self.assertEqual(res, 2)

    def test_third_test(self):
        res = solution(40)
        self.assertEqual(res, 1)

    def test_fourth_test(self):
        res = solution(1089028)
        self.assertEqual(res, 6)


if __name__ == '__main__':
    unittest.main()
