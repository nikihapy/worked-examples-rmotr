import unittest


class PopulationGrowthTestCase(unittest.TestCase):

    def test_population_X2(self):
        self.assertEqual(population_growth(5000, 0.1, 10000), 8)

    def test_population_X4(self):
        self.assertEqual(population_growth(5000, 0.1, 20000), 15)

    def test_population_X8(self):
        self.assertEqual(population_growth(5000, 0.1, 40000), 22)

    def test_bad_growth_rate(self):
        self.assertEqual(population_growth(5000, 0, 40000), 
            'invalid growth rate')