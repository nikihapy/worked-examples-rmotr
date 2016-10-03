import unittest


class ReturnBooleanTest(unittest.TestCase):
    def test_return_of_boolean(self):
        self.assertEqual(return_boolean(12), True)
        self.assertEqual(return_boolean(6), False)
        self.assertEqual(return_boolean(9), False)
