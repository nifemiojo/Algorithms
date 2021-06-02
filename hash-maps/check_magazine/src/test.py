import unittest
from .solution import checkMagazine


class TestCheckMagazine(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_test(self):
        mag = ['give', 'me', 'one', 'grand', 'today', 'night']
        note = ['give', 'one', 'grand', 'today']
        res = checkMagazine(mag, note)
        self.assertEqual(res, 'Yes')

    def test_duplicate_word_in_note(self):
        mag = ['two', 'times', 'three', 'is', 'not', 'four']
        note = ['two', 'times', 'two', 'is', 'four']
        res = checkMagazine(mag, note)
        self.assertEqual(res, 'No')

if __name__ == '__main__':
    unittest.main()
