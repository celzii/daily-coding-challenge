import unittest
from solution import find_maximum

class TestFindMaximum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_maximum([1, 7, 3, 9, 2]), 9)
        self.assertEqual(find_maximum([-5, -2, -10]), -2)
        self.assertEqual(find_maximum([42]), 42)

    def test_empty(self):
        with self.assertRaises(ValueError):
            find_maximum([])

if __name__ == "__main__":
    unittest.main()