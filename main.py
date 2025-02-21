import requests
import pandas as pd
import os
from sqlalchemy import create_engine

def convert_unix_to_iso(series: pd.Series) -> pd.Series:
    """
    Convert Unix timestamps to ISO 8601 formatted datetime strings.

    Args:
        series (pd.Series): Series containing Unix timestamps

    Returns:
        pd.Series: Series with timestamps in ISO format (YYYY-MM-DDTHH:MM:SS)
    """
    return pd.to_datetime(series, unit='s').dt.strftime('%Y-%m-%dT%H:%M:%S')

def main():
    """
    Fetch ISS location data from the Open Notify API and store in PostgreSQL database.
    
    Environment Variables:
        POSTGRES_USER: Database username
        POSTGRES_PASSWORD: Database password
        POSTGRES_HOST: Database host address

    Raises:
        Exception: If API request fails or database connection errors occur
    """
    # Read database credentials from environment variables
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")

    # Get the API response using requests package
    URL = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(URL)
        if response.status_code != 200:
            raise Exception(f"API request failed with status {response.status_code: {response.text}}")
        # Extract the JSON from the response
        data = response.json()
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Request successful: {data}")

    # Convert the response into a DataFrame using pandas
    df = pd.DataFrame([{
        "timestamp": data["timestamp"],
        "latitude": data["iss_position"]["latitude"],
        "longitude": data["iss_position"]["longitude"]
    }])

    df["timestamp"] = convert_unix_to_iso(df["timestamp"])

    # Handle the database writing section
    # First create an engine to connect to the RDS database iss_locations_db
    engine = create_engine(f"postgresql://{user}:{password}@{host}:5432/iss_locations_db")

    # Only needed if table needs to be recreated
    # df.head(0).to_sql(name="iss_locations", con=engine, if_exists="replace", index=False)
    df.to_sql(name="iss_locations", con=engine, if_exists="append", index=False)

if __name__ == "__main__":
    main()
