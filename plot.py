import pandas as pd
import os
from sqlalchemy import create_engine

DATABASE = "iss_locations_db"
TABLE = "iss_locations"

def main():
    # Step 1: establish the connection to the AWS RDS db
    db_engine = connect_to_database()

    # With connection established, read all the data from the table
    # This should give you a dataframe to pass to the next plotting function
    dataframe = convert_sql_table_to_df(TABLE, db_engine)

    # Having read all the data from Postgres db
    # Call the plotting function
    # create_plot(dataframe)
    print(dataframe)

# ------ FUNCTION DEFINITIONS ------ 
def connect_to_database():
    # Read database credentials from environment variables
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")

    # Create the engine connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{DATABASE}")
    return engine

def convert_sql_table_to_df(table_name, engine):
    # This should be changed to read from the database rather than writing to the database
    df = pd.read_sql_table(table_name, engine)   

    # This function should return a dataframe
    return df
    

#def create_plot(df):
#    pass



if __name__ == "__main__":
    main()
