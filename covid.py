import requests
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# the base URL to be used
base_url = 'https://covid-api.mmediagroup.fr/v1'


# test 1: check that the user input is not empty and is a valid country
def get_user_input():
    # ask the user for input
    input_country = input('Enter a country: ')
    return input_country


# test 2: check that the status code is 200
# test 3: check that the file obtained is in JSON
# test 4: check that we got a dictionary from the JSON file
# test 5: check that we got a dictionary for "All" covid cases
def get_data_from_api(base_url, user_country):
    # get the data from the API
    response = requests.get(base_url + '/cases?country=' + user_country)
    response_json = response.json()
    country_data = response_json['All']
    return response, response_json, country_data


# test 6: check that country is a string and the others are integers
def get_data_items(country_data):
    # data items to be used
    country = country_data["country"]
    confirmed = country_data["confirmed"]
    recovered = country_data["recovered"]
    deaths = country_data["deaths"]
    population = country_data["population"]
    return country, confirmed, recovered, deaths, population


# not sure what checks to use
def print_data():
    # print statements
    print(f'Covid Situation in {country}')
    print(f'Confirmed Cases : {confirmed}')
    print(f'Recovered : {recovered}')
    print(f'Deaths : {deaths}')
    print(f'Total Population : {population}')


# test 7: check that col_names is a list of strings
# test 8: check that country_data_df is a dataframe object
# test 9: check that country_data_df's columns have been populated
def dict_to_df():
    # creating data frame from the dictionary obtained
    col_names = ['Country', 'Confirmed', 'Recovered', 'Deaths', 'Population']
    country_data_df = pd.DataFrame(columns=col_names)
    country_data_df.loc[len(country_data_df.index)] = [country, confirmed,
                                                       recovered, deaths,
                                                       population]


# test 10: check that the engine has been created
# test 11: check that the SQL table has been created
def engine_and_SQLtable():
    # Create an engine
    engine = create_engine('mysql://root:codio@localhost/covid')

    # Create and send SQLtable from my dataframe
    SQLtable = country_data_df.to_sql('by_country', con=engine,
                                      if_exists='replace', index=False)


# Not every country has this value
# print(f'Last updated at {country_data["updated"]}')
