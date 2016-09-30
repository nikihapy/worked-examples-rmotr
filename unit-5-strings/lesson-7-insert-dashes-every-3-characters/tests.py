import unittest


class InsertDashesTestCase(unittest.TestCase):

    def test_with_large_string(self):
        self.assertEqual(insert_dashes('Python is Awesome'),
                         'Pyt-hon- is- Aw-eso-me')

    def test_with_short_string(self):
        self.assertEqual(insert_dashes('Python'), 'Pyt-hon-')
