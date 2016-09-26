import unittest


class CheckOutOfBoundariesTestCase(unittest.TestCase):

    def test_negative(self):
        self.assertEqual(check_out_of_boundaries(-3), True)

    def test_over_10(self):
        self.assertEqual(check_out_of_boundaries(12), True)

    def test_in_boundaries(self):
        self.assertEqual(check_out_of_boundaries(7), False)
