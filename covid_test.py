import unittest
from covid import get_user_input, get_data_from_api, get_data_items
from covid import print_data, dict_to_df, engine_and_SQLtable

class covid_test(unittest.TestCase):


    # Later include test to check if input is a valid country
    def test_get_user_input(self):
        print()
        self.assertNotEqual(get_user_input(), "")


    # Not sure how to check if data from api is in JSON format
    def test_get_data_from_api(self):
        base_url = 'https://covid-api.mmediagroup.fr/v1'
        country = get_user_input()
        results = get_data_from_api(base_url, country)
        response = results[0]
        response_json = results[1]
        country_data = results[2]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response_json), type({}))
        self.assertEqual(type(country_data), type({}))


    def test_get_data_items(self):
        base_url = 'https://covid-api.mmediagroup.fr/v1'
        print()
        country = get_user_input()
        country_data = get_data_from_api(base_url, country)[2]
        results = get_data_items(country_data)
        self.assertEqual(type(results[0]), type(""))
        for i in range(1, 5):
            self.assertEqual(type(results[i]), type(2))


if __name__ == '__main__':
    unittest.main()
