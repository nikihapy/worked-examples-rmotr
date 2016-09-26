import unittest


class AddOnlyIntegersTestCase(unittest.TestCase):

    def test_integers(self):
        self.assertEqual(add_only_integers(2, 3), 5)

    def test_not_integers(self):
        self.assertEqual(add_only_integers(2, 'what'), 'invalid parameters')
