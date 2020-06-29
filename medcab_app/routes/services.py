import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

def fetch_strains(query):
    """
    Creates connection object to medcab database and is used for 'strains' query 
    
    Returns: id, strain and rating

    Param:
        query: a SQL query
    """
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["id",
               "strain",
               "rating"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    print(type(df))

    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    connection.close()
    return pairs

def fetch_top(query):
    """
    Creates connection object to medcab database and is used for 'top' queries 
    
    Returns: strain name

    Param:
        query: a SQL query
    """
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["strain"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    print(type(df))

    # DF to dictionary
    pairs = df.to_json(orient='records')
    print(type(pairs))
    # Closing Connection
    connection.close()
    return pairs

def fetch_data(query):
    """
    Creates connection object to medcab database and is used for 'data' query 
    
    Returns: all data in database (strain name, id, flavors, effects, medical,
    type, rating, flavor)

    Param:
        query: a SQL query
    """
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST)
    cursor = connection.cursor()

    # Execute query
    cursor.execute(query)
    # Query results
    strains = list(cursor.fetchall())
    # Key-value pair names for df columns
    columns = ["strain", "id",
                "flavors",
                "effects",
                "medical",
                "type",
                "rating",
                "flavor"]
    # List of tuples to DF
    df = pd.DataFrame(strains, columns=columns)
    # DF to dictionary
    pairs = df.to_json(orient='records')
    # Closing Connection
    connection.close()
    return pairs

def parse_records(database_records):
    """
    Parses database records into a clean json-like structure
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records