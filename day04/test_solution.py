import unittest
from solution import fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(-3), [])

if __name__ == "__main__":
    unittest.main()