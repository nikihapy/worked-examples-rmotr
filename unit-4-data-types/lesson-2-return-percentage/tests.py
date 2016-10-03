import unittest


class TestMinutePercentage(unittest.TestCase):
    def test_return_minute_percentage(self):
        self.assertEqual(return_percentage(34), 56)
        self.assertEqual(return_percentage(12), 20)
        self.assertEqual(return_percentage(60), 100)
