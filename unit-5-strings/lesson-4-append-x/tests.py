import unittest


class AppendXTestCase(unittest.TestCase):

    def test_with_valid_string(self):
        self.assertEqual(append_x('abc_'), 'abc_x')

    def test_with_empty_string(self):
        self.assertEqual(append_x(''), '')
