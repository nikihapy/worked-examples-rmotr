import unittest


class GetElementNumberListTestCase(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(get_element_number(['a', 'b', 'c'], 'c'), 2)

    def test_repeated_term(self):
        self.assertEqual(get_element_number(['a', 'a', 'a'], 'a'), 0)

    def test_no_match(self):
        self.assertEqual(get_element_number(['a', 'b', 'c'], 's'), 'no match')
