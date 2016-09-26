import unittest


class MoreThan3ElementsTestCase(unittest.TestCase):

    def test_more_than_3_elements(self):
        self.assertEqual(more_than_3_elements([1,2,3,4,5]), True)

    def test_not_more_than_3_elements(self):
        self.assertEqual(more_than_3_elements([1,2,3]), False)
