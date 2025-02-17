import pandas as pd
import os
from sqlalchemy import create_engine

def main():
    # Step 1: establish the connection to the AWS RDS db
    connect_to_database()

    # With connection established, read all the data from the table
    # This should give you a dataframe to pass to the next plotting function
    dataframe = convert_sql_table_to_df(sql_table)

    # Having read all the data from Postgres db
    # Call the plotting function
    create_plot(dataframe)

# ------ FUNCTION DEFINITIONS ------ 
def connect_to_database():
    # Read database credentials from environment variables
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")

    # Create the engine connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/iss_locations_db")

def convert_sql_table_to_df(sql_table):
    # This should be changed to read from the database rather than writing to the database
    # TODO: Research the function to do this
    df.to_sql(name="iss_locations", con=engine, if_exists="append", index=False)

    # This function should return a dataframe
    pass

def create_plot(df):
    pass



if __name__ == "__main__":
    main()
