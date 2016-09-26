import unittest


class ConvertBoolToBinaryTestCase(unittest.TestCase):

    def test_true_value(self):
        self.assertEqual(convert_bool_to_binary(True), 1)

    def test_false_value(self):
        self.assertEqual(convert_bool_to_binary(False), 0)
