import unittest


class ColorMixerTestCase(unittest.TestCase):

    def test_red_blue(self):
        self.assertEqual(color_mixer('red', 'blue'), 'Magenta')

    def test_blue_red(self):
        self.assertEqual(color_mixer('blue', 'red'), 'Magenta')

    def test_red_yellow(self):
        self.assertEqual(color_mixer('red', 'yellow'), 'Orange')

    def test_yellow_red(self):
        self.assertEqual(color_mixer('yellow', 'red'), 'Orange')

    def test_yellow_blue(self):
        self.assertEqual(color_mixer('yellow', 'blue'), 'Green')

    def test_blue_yellow(self):
        self.assertEqual(color_mixer('blue', 'yellow'), 'Green')