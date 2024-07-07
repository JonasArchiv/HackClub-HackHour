import requests
from secrets import apikey, slack_id

BASE_URL = 'https://hackhour.hackclub.com'

headers = {
    "Authorization": f"Bearer {apikey}"
}


class HackHourManager:
    def __init__(self):
        response = requests.get(f"{BASE_URL}/ping")
        if response.status_code == 200:
            print("API is online")
        else:
            print("API is offline")

    def get_stats(self):
        response = requests.get(f"{BASE_URL}/api/stats/{slack_id}", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to get stats. Status code: {response.status_code}")
            return None
