import unittest


class MaxCharTestCase(unittest.TestCase):

    def test_with_many_chars(self):
        self.assertEqual(max_char('janbfthahdag'), 't')

    def test_with_a_single_char(self):
        self.assertEqual(max_char('j'), 'j')

    def test_with_empty_string(self):
        self.assertEqual(max_char(''), '')
