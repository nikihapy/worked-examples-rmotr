import unittest


class IsStringTestCase(unittest.TestCase):

    def test_string(self):
        self.assertEqual(is_string('happy'), 'yes')

    def test_integer(self):
        self.assertEqual(is_string(27), 'no')