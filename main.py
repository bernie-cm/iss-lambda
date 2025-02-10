import requests
import pandas as pd
import argparse
from sqlalchemy import create_engine


def convert_unix_to_iso(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, unit='s').dt.strftime('%Y-%m-%dT%H:%M:%S')

def main(params):
    user = params.u
    password = params.p

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
    engine = create_engine(f"postgresql://{user}:{password}@localhost:5432/iss-locations")

    # Only needed if table needs to be recreated
    # df.head(0).to_sql(name="iss-locations", con=engine, if_exists="replace", index=False)
    df.to_sql(name="iss-locations", con=engine, if_exists="append", index=False)

if __name__ == "__main__":
    # Create the CLI parser
    parser = argparse.ArgumentParser(description="Call ISS API and store current position in Amazon RDS")

    # Create two CLI arguments to ask for username and password
    parser.add_argument("-u", help="username for Postgres")
    parser.add_argument("-p", help="password for Postgres")

    args = parser.parse_args()
    main(args)