import unittest


class TestFunWithStrings(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(fun_with_strings("hello"), "hellohellohellohellohello")
        self.assertEqual(fun_with_strings("*"), "*****")
        self.assertEqual(fun_with_strings("*.*"), "*.**.**.**.**.*")
        self.assertEqual(fun_with_strings("hey"), "heyheyheyheyhey")
