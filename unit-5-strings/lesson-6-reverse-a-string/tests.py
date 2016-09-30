import unittest


class ReverseTestCase(unittest.TestCase):

    def test_with_large_string(self):
        self.assertEqual(reverse_string('Python is Awesome'),
                         'emosewA si nohtyP')

    def test_with_short_string(self):
        self.assertEqual(reverse_string('Python'), 'nohtyP')
