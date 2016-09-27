import unittest


class SumOfNumbersInListTestCase(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_numbers_in_list([]), 0)

    def test_list_of_1(self):
        self.assertEqual(sum_of_numbers_in_list([4]), 4)

    def test_list_of_2(self):
        self.assertEqual(sum_of_numbers_in_list([2,3]), 5)

    def test_list_of_3(self):
        self.assertEqual(sum_of_numbers_in_list([2,3,4]), 9)
