import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table_from_csv(conn, csv_file_str, table_name):
    # load the data into a Pandas DataFrame
    data = pd.read_csv(csv_file_str)
    # write the data to a sqlite table
    data.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Table {table_name} created")

def main():
    database = r"/Users/brendanmclaughlin/Desktop/Coding/fullstack-apps/glucoseGPT/data/cgm.db"  # use your path
    csv_file = "/Users/brendanmclaughlin/Desktop/Coding/fullstack-apps/glucoseGPT/data/NonDiabDeviceCGM.csv"  # use your csv file
    table_name = "CGMTable"  # table name
    conn = create_connection(database)

    if conn is not None:
        create_table_from_csv(conn, csv_file, table_name)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
