import pandas as pd
import os
from sqlalchemy import create_engine

def main():
    connect_to_database():
        pass

    convert_sql_table_to_df(sql_table):
        pass

    create_plot(dataframe):
        pass

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
