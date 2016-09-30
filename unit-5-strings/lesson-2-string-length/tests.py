import unittest


class StringLengthTestCase(unittest.TestCase):

    def test_with_length_greater_than_0(self):
        self.assertEqual(string_length("abcde"), 5)

    def test_with_empty_string(self):
        self.assertEqual(string_length(""), 0)
