import unittest


class EvenPositionsTestCase(unittest.TestCase):

    def test_with_even_length(self):
        self.assertEqual(chars_in_even_positions('Python'), 'yhn')

    def test_with_odd_length(self):
        self.assertEqual(chars_in_even_positions('Respect'), 'epc')

    def test_two_characters(self):
        self.assertEqual(chars_in_even_positions('No'), 'o')

    def test_one_characters(self):
        self.assertEqual(chars_in_even_positions('X'), '')
