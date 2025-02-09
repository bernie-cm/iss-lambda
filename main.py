import requests
import pandas as pd

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

# Convert the response into a dataframe using pandas

# Establish the connection to the database using ???

# Write the information to the Postgres database

# Close the connection

# def main():
#     pass

# if __name__ == "__main__":
#     main()