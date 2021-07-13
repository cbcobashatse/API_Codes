import requests
import pandas as pd
import sqlalchemy
import os
from sqlalchemy import create_engine


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
    # the base URL to be used
    
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


# test 7: check that col_names is a list of strings
# test 8: check that country_data_df is a dataframe object
def create_dataframe():
    col_names = ['Country', 'Confirmed', 'Recovered', 'Deaths', 'Population']
    dataframe = pd.DataFrame(columns=col_names)
    return dataframe


# test 9: check that country_data_df's columns have been populated
# test 10: check that a dataframe was returned
def put_values_dataframe(dataframe, values):
    dataframe.loc[len(dataframe.index)] = values
    return dataframe

'''
def loadNewData(df):
    #get data corresponding to country input by user
    user_country = get_user_input()
    country_data = get_data_from_api()[2]
    data = get_data_items(country_data)
    dataframe = dict_to_df(data)

    # adding new data
    dataframe.loc[len(dataframe.index)] = values
    #create_engine()
    #SQLtable = create_SQLtable(dataframe)
    #save_SQL_to_file()
'''

# test 10: check that the engine has been created
def create_engine_function(dbName):
    # Create an engine
    # engine = create_engine('mysql://root:codio@localhost/covid')
    return create_engine('mysql://root:codio@localhost/'
                         + dbName + '?charset=utf8', encoding='utf-8')


# test 11: check that the SQL table has been created
## def create_SQLtable(dtfr, dbName, tableName):
    # Create and send SQLtable from my dataframe
    # with dataframe = country_data_df
##     os.system('mysql -u root -pcodio -e\
##               "CREATE DATABASE IF NOT EXISTS ' + dbName + ';"')
##     dtfr.to_sql(tableName, con=create_engine_function(dbName),
##                 if_exists='replace', index=False)
    # SQLtable = dataframe.to_sql('by_country', con=engine,
    #                             if_exists='replace', index=False)
    # return SQLtable

'''
# test?
def loadDataset(update):
    # Load data from database to dataframe
    df = pd.read_sql_table('by_country', con=engine)
    if update:
        return loadNewData(df)
    else:
        return df
'''

def save_data_to_file(dtfr, dbName, tableName, fileName):
    # os.system("mysqldump -u root -pcodio covid > covid_data.sql")
    dtfr.to_sql(tableName, con=create_engine_function(dbName),
                if_exists='replace',
                index=False)
    os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))


def load_database(dbName, fileName):
    # os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS covid_data.sql;"')
    # os.system("mysql -u root -pcodio covid < covid_data.sql")
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')


'''
def choose_action():
    action = input("Choose an action (e for existing data and o for overwrite): ")
    if (action == 'e'):
        print("Existing data")
        load_SQL_from_file()
        update_action = input("Do you want to update data? (Write y or n): ")
        if (update_action == 'y'):
            df = loadDataset(True)
        else:
            df = loadDataset(False)
    elif(action == 'o'):
        print("Overwriting")
        #user_country = get_user_input()
        #country_data = get_data_from_api()[2]
        #data = get_data_items(country_data)
        #dataframe = dict_to_df(data)
        #create_engine()
        #SQLtable = create_SQLtable(dataframe)
        #save_SQL_to_file()
'''

def check_database_input(country, dataframe):
    result = dataframe[dataframe['Country'] == country]
    return (len(result.index) != 0), result
        

# choose_action()

def main():
    # defining some terms
    tableName = 'by_country'
    fileName = 'covid_data'
    dbName = 'covid'

    base_url = 'https://covid-api.mmediagroup.fr/v1'

    user_country = get_user_input()
    load_database(dbName, fileName)
    dtfr_initial = pd.read_sql_table(tableName,
                                     con=create_engine_function(dbName))

    is_in_db = check_database_input(user_country, dtfr_initial)
    if is_in_db[0]:
        print(is_in_db[1])
    else:
        data = get_data_from_api(base_url, user_country)[2]
        values = get_data_items(data)

        # creating a new dataframe/database/SQL file
        # dataframe = create_dataframe()

        dtfr_final = put_values_dataframe(dtfr_initial, values)
        save_data_to_file(dtfr_final, dbName, tableName, fileName)
        print(dtfr_final.tail(1))


if __name__ == "__main__":
    main()
