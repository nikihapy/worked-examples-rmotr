import unittest


class PowersOf2TestCase(unittest.TestCase):

    def test_case_0(self):
        self.assertEqual(powers_of_two(0), 1)

    def test_case_1(self):
        self.assertEqual(powers_of_two(1), 2)

    def test_case_2(self):
        self.assertEqual(powers_of_two(2), 4)

    def test_case_3(self):
        self.assertEqual(powers_of_two(3), 8)
