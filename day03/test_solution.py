import unittest
from solution import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))

if __name__ == "__main__":
    unittest.main()
