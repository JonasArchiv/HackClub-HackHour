from secrets import apikey, slack_id
import requests
from datetime import timedelta


stats_url = f"https://hackhour.hackclub.com/api/stats/{slack_id}"

headers = {
    "Authorization": f"Bearer {apikey}"
}

print(f"Sending request to {stats_url} with headers {headers}")

try:
    response = requests.get(stats_url, headers=headers)
    print(f"Response status code: {response.status_code}")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
else:
    if response.status_code == 200:
        data = response.json()
        print(f"Response JSON: {data}")
        if data["ok"]:
            total_minutes = data["data"]["total"]

            time_spent = timedelta(minutes=total_minutes)
            days = time_spent.days
            hours, remainder = divmod(time_spent.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"Du hast insgesamt {total_minutes} Minuten verbracht.")
            print(f"Das entspricht: {days} Tage, {hours} Stunden, {minutes} Minuten und {seconds} Sekunden.")
        else:
            print("Fehler: Die API hat einen Fehler zurückgegeben.")
    else:
        print(f"Fehler: Die Anfrage war nicht erfolgreich. Status Code: {response.status_code}")
