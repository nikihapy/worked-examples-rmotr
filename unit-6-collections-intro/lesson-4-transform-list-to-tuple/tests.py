import unittest


class List2TupleTestCase(unittest.TestCase):

    def test_list_2_tuple(self):
        self.assertEqual(list_2_tuple([3, 2, 'a']), (3, 2, 'a'))
        self.assertEqual(list_2_tuple([7]), (7, ))
