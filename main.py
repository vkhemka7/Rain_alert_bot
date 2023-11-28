import requests
from twilio.rest import Client
account_sid = "AC8606bad5d03332b5b8ebc3f9d2330a45"
auth_token = "d35033bb83d6588a0a414ff0e47d83d1"
api_key = "8aca1560e7403da18a82d7f82229764e"
parameters = {
    "lat": 22.572645,
    "lon": 88.363892,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]
will_rain = False

for hour in weather_data:
    id = hour["weather"][0]["id"]
    if int(id) < 700:
        will_rain = True

if will_rain:
    print("Will rain")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an Umbrella",
        from_="+16628073835",
        to='+919830430161'
    )

print(message.status)