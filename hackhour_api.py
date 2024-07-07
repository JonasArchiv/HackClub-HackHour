import requests
from secrets import apikey, slack_id

BASE_URL = 'https://hackhour.hackclub.com'


class HackHourManager:
    def __init__(self):
        response = requests.get(f"{BASE_URL}/ping")
        if response.status_code == 200:
            print("API is online")
        else:
            print("API is offline")


HHM = HackHourManager()
