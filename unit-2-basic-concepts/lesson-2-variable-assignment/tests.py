import unittest


class AssignIntegerToVariable(unittest.TestCase):
    def test_x(self):
        self.assertTrue(isinstance(x, int))
        self.assertEqual(x, 10)

    def test_y(self):
        self.assertTrue(isinstance(y, float))
        self.assertEqual(y, 3.14)

    def test_z(self):
        self.assertTrue(isinstance(z, str))
        self.assertEqual(z, 'python')
