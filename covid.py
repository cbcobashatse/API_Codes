import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# the base URL to be used
base_url = 'https://covid-api.mmediagroup.fr/v1'

# ask the user for input
user_country = input('Enter a country: ')

# get the data from the API
response = requests.get(base_url + '/cases?country=' + user_country)
response_json = response.json()
country_data = response_json['All']

# data items to be used
country = country_data["country"]
confirmed = country_data["confirmed"]
recovered = country_data["recovered"]
deaths = country_data["deaths"]
population = country_data["population"]

# print statements
print(f'Covid Situation in {country}')
print(f'Confirmed Cases : {confirmed}')
print(f'Recovered : {recovered}')
print(f'Deaths : {deaths}')
print(f'Total Population : {population}')

# creating data frame from the dictionary obtained
col_names = ['Country', 'Confirmed', 'Recovered', 'Deaths', 'Population']
country_data_df = pd.DataFrame(columns=col_names)
country_data_df.loc[len(country_data_df.index)] = [country, confirmed, 
                                                   recovered, deaths, 
                                                   population]

# Create an engine
engine = create_engine('mysql://root:codio@localhost/covid')

# Create and send SQLtable from my dataframe
country_data_df.to_sql('by_country', con=engine, if_exists='replace', 
                       index=False)

# Not every country has this value
# print(f'Last updated at {country_data["updated"]}')
