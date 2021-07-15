import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests, os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import matplotlib
import matplotlib.pyplot as plt
from covid import load_database, create_engine_function
import plotly.graph_objects as go  # import plotly


# create a method for visualization
def histogram(dataframe, column_name):
    dataframe.hist(column=column_name)  # create the histogram
    plt.show()


# histogram(df, 'length' )

def boxplot(dataframe, column_name):
    fig = plt.figure()
    box = fig.add_subplot()
    box.boxplot(x=dataframe[column_name], vert=False)
    box.set_xlabel(column_name)
    box.set_title('Distribution of ' + column_name)
    plt.show()


def barplot(x_column_name, y_column_name):
    # create a figure
    fig = go.Figure(data=go.Bar(x=x_column_name, y=y_column_name))
    fig.write_html('figure.html')  # export to HTML file


def main():
    # defining some terms
    tableName = 'by_country'
    fileName = 'covid_data'
    dbName = 'covid'

    load_database(dbName, fileName)
    dataframe = pd.read_sql_table(tableName,
                                  con=create_engine_function(dbName))
    # print(dataframe)
    # histogram(dataframe, 'Deaths')
    # boxplot(dataframe, 'Confirmed')
    barplot(dataframe['Country'], dataframe['Population'])


if __name__ == "__main__":
    main()
