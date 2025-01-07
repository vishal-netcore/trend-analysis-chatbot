import vertica_python
import pandas as pd 
import os
from dotenv import load_dotenv

load_dotenv()

vertica_config = {
    "host": "vertica-cluster-url-02-prod-us.netcorein.com",
    "user": "devops",
    "password": os.getenv('VERTICA_SMARTECH_DEVOPS_PASSWORD'),
    "database": "smartech",
    "port": 5433,
    "autoCommit": False
}

def create_connection():
    '''
    create vertica database connection
    returns: vertica connection object
    '''
    connection_config = {
        'host': vertica_config["host"],
        'port': vertica_config["port"],
        'user': vertica_config["user"],
        'password': vertica_config["password"],
        'database': vertica_config["database"],
        'autocommit': vertica_config["autoCommit"]
    }
    
    connection = vertica_python.connect(**connection_config)
    return connection


def read(connection, query, columns):
    '''
    args:
        1. connection: vertica connection object
        2. query: query string
        3. columns: array of column names
    returns: dataframe with specified columns

    This function executes the given query and returns a pandas dataframe with the specified columns.
    '''
    cursor = connection.cursor()
    cursor.execute(query)

    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    
    cursor.close()
    return df
