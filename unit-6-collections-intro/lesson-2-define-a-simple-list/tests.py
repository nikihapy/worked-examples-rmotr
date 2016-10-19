import unittest


class SimpleListTestCase(unittest.TestCase):

    def test_list_is_correct(self):
        self.assertEqual(simple_list(), [1, 'a', True])
