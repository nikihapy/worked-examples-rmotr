import unittest


class GetGradeLetterTestCase(unittest.TestCase):

    def test_A_score(self):
        self.assertEqual(get_grade_letter(93), 'A')

    def test_B_score(self):
        self.assertEqual(get_grade_letter(80), 'B')

    def test_C_score(self):
        self.assertEqual(get_grade_letter(75), 'C')

    def test_D_score(self):
        self.assertEqual(get_grade_letter(67), 'D')

    def test_F_score(self):
        self.assertEqual(get_grade_letter(42), 'F')
