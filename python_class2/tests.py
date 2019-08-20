"""Simple unittest example"""
import unittest

class SimpleTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
    def test_subtraction(self):
        self.assertNotEqual(4 - 2, 0)
        self.assertEqual(2 - 2, 0)
    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_add_strings(self):
        self.assertEqual("a" + "b", "ab")
    def test_subtract_strings(self):
        with self.assertRaises(TypeError):
            "a" - "b"


if __name__ == "__main__":
    unittest.main()
