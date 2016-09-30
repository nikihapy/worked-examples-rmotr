import unittest


class ConcatenateStringTestCase(unittest.TestCase):

    def test_with_multiple_strings(self):
        self.assertEqual(concatenate_strings('abc', 'def'), 'abcdef')

    def test_with_empty_string(self):
        self.assertEqual(concatenate_strings('abc', ''), 'abc')
