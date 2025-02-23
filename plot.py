import pandas as pd
import os
from sqlalchemy import create_engine
import plotly.graph_objects as go

DATABASE = "iss_locations_db"
TABLE = "iss_locations"

def main():
    # Establish the connection to the AWS RDS db
    db_engine = connect_to_database()

    # With connection established, read all the data from the table
    # This should give you a dataframe to pass to the next plotting function
    dataframe = convert_sql_table_to_df(TABLE, db_engine)

    # Having read all the data from Postgres db
    # Call the plotting function
    #create_plot(dataframe)
    print(dataframe.head(5))

# ------ FUNCTION DEFINITIONS ------ 
def connect_to_database():
    """
    Establishes a connection to a PostgreSQL database using environment variables.

    This function reads database credentials from environment variables and creates
    a SQLAlchemy engine connection to a PostgreSQL database.

    Required Environment Variables:
        POSTGRES_USER: Database username
        POSTGRES_PASSWORD: Database password
        POSTGRES_HOST: Database host address

    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine instance connected to the database.
    """
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/{DATABASE}")
    return engine

def convert_sql_table_to_df(table_name, engine):
    """
    Reads a SQL table into a pandas DataFrame.

    This function queries an entire table from the database and converts it into
    a pandas DataFrame for further analysis or processing.

    Args:
        table_name (str): Name of the SQL table to read.
        engine (sqlalchemy.engine.Engine): SQLAlchemy engine instance connected
            to the database.

    Returns:
        pandas.DataFrame: DataFrame containing all rows and columns from the
            specified table.
    """
    df = pd.read_sql_table(table_name, engine)   
    return df
    

def create_plot(df):
    pass



if __name__ == "__main__":
    main()
