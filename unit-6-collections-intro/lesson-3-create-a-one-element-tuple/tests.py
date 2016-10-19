import unittest


class OneElementTupleTestCase(unittest.TestCase):

    def test_tuple_is_correct(self):
        self.assertEqual(one_element_tuple('b'), ('b', ))
        self.assertEqual(one_element_tuple(7), (7, ))
