import unittest


class GreaterThan20TestCase(unittest.TestCase):

    def test_greater_than_20(self):
        self.assertEqual(greater_than_20(42), True)

    def test_less_than_20(self):
        self.assertEqual(greater_than_20(19), False)
