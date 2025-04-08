#!/bin/bash/python3

import requests
from datetime import datetime

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Fetched {len(data['states'])} flight at {datetime.now()}")
        return data['states']
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

