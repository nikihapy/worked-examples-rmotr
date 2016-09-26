import unittest


class ConditionalMultiplicationTestCase(unittest.TestCase):

    def test_true_condition(self):
        self.assertEqual(conditional_multiplication(True, 5), 50)

    def test_false_condition(self):
        self.assertEqual(conditional_multiplication(False, 5), 5)

