import unittest


class CreateCountingListTestCase(unittest.TestCase):

    def test_count_to_7(self):
        self.assertEqual(create_counting_list(7), [1, 2, 3, 4, 5, 6, 7])

    def test_count_to_3(self):
        self.assertEqual(create_counting_list(3), [1, 2, 3])

    def test_do_not_count(self):
        self.assertEqual(create_counting_list(0), [])

    def test_negative(self):
        self.assertEqual(create_counting_list(-1), 'cannot be negative')