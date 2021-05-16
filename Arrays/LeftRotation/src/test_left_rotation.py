import unittest
from .left_rotation import rotLeft

class TestLeftRotation(unittest.TestCase):

    def test_zero_rotations(self):
        result = rotLeft([1, 2, 3, 4], 0)
        self.assertIs(type(result), list)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_four_rotations(self):
        result = rotLeft([1, 2, 3, 4, 5], 4)
        self.assertEqual(result, [5, 1, 2, 3, 4])

    def test_n_rotations(self):
        result = rotLeft([1, 2, 3, 4, 5, 6], 6)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()