import unittest


class MakeNumberOddTestCase(unittest.TestCase):

    def test_even_number(self):
        self.assertEqual(make_number_odd(2), 3)

    def test_odd_number(self):
        self.assertEqual(make_number_odd(5), 5)
