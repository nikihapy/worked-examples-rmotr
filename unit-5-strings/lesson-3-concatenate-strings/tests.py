import unittest


class ConcatenateStringTestCase(unittest.TestCase):

    def test_with_multiple_strings(self):
        s1 = 'abc'
        s2 = 'def'
        self.assertEqual(concatenate_strings(s1, s2), 'abcdef')
        self.assertEqual(s1, 'abc')
        self.assertEqual(s2, 'def')

    def test_with_empty_string(self):
        s1 = 'abc'
        s2 = ''
        self.assertEqual(concatenate_strings(s1, s2), 'abc')
        self.assertEqual(s1, 'abc')
        self.assertEqual(s2, '')
