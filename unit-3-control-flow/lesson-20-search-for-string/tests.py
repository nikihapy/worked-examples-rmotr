import unittest


class GetElementNumberListTestCase(unittest.TestCase):

    def test_string_in_list(self):
        self.assertEqual(search_for_string(['santiago', 'santi', 'santa'],
            'santa'), 'string found!')

    def test_string_present(self):
        self.assertEqual(search_for_string(['a', 'b', 'c'], 'd'),
            'string not found')

    def test_empty_list(self):
        self.assertEqual(search_for_string([], 'a'), 'string not found')
