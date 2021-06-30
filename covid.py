import requests

base_url = 'https://covid-api.mmediagroup.fr/v1'

country = input('Enter a country: ')

response = requests.get(base_url + '/cases?country=' + country)
response_json = response.json()
country_data = response_json['All']

print(f'Covid Situation in {country_data["country"]}')
print(f'Confirmed Cases : {country_data["confirmed"]}')
print(f'Recovered : {country_data["recovered"]}')
print(f'Deaths : {country_data["deaths"]}')
print(f'Total Population : {country_data["population"]}')

#Not every country has this value
#print(f'Last updated at {country_data["updated"]}')
