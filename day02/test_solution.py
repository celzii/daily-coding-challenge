import unittest
from io import StringIO
import sys
from solution import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_output(self):
        expected = []
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                expected.append("FizzBuzz")
            elif i % 3 == 0:
                expected.append("Fizz")
            elif i % 5 == 0:
                expected.append("Buzz")
            else:
                expected.append(str(i))
        
        captured = StringIO()
        sys.stdout = captured
        fizzbuzz()
        sys.stdout = sys.__stdout__
        output = captured.getvalue().strip().split('\n')
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()
