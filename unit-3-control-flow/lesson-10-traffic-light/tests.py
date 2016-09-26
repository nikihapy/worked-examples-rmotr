import unittest


class TrafficLightTestCase(unittest.TestCase):

    def test_red_light(self):
        self.assertEqual(traffic_light('red'), 'stop')

    def test_yellow_light(self):
        self.assertEqual(traffic_light('yellow'), 'slow down')

    def test_green_light(self):
        self.assertEqual(traffic_light('green'), 'go')
