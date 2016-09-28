import unittest


class SumIfListOfIntsListTestCase(unittest.TestCase):

    def test_sum_of_ints(self):
        self.assertEqual(sum_if_list_of_ints([1, 2, 3]), 6)

    def test_mixed_list(self):
        self.assertEqual(sum_if_list_of_ints([1, 'a', 3]), 'not an int')

    def test_empty_list(self):
        self.assertEqual(sum_if_list_of_ints([]), 0)
