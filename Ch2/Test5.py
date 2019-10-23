import requests
import json


link = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

resp = requests.get(link)
text = resp.text
data = json.loads(text)

print(resp)
print(data["main"]["temp"])