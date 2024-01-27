import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    '''Test for the city_function.py'''

    def test_cities(self):
        '''Do cities like 'Santiago' work?'''
        formatted_city = get_formatted_city('santiago')
        self.assertEqual(formatted_city, 'Santiago.')

    def test_city_country_name(self):
        '''Do cities and countries like 'Santiago, Chile' work?'''
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile.')

    def test_city_country_population(self):
        '''Do cities, countries and populations like 'Santiago, Chile - 5000000'work?'''
        formatted_city = get_formatted_city('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - 5000000.')

if __name__ == 'main.py':
    unittest.main.py



