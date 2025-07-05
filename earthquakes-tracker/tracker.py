import requests
import pandas
import json

url = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")

json_response = json.dumps((url.json()), indent=2)

with open('earthquakes-tracker/output.txt', 'w') as file:
    file.write(json_response)
    file.close()

url = url.json()

earthquakes = url['features']

earthquake_list = []
for earthquake in earthquakes:
    properties = earthquake['properties']
    if  properties['type'] == 'earthquake':
        magnitude = properties['mag']
        location = properties['place']
        earthquake_url = properties['url']
        # print(magnitude, location, earthquake_url)
        earthquake_list.append({'Magnitude': magnitude, 'Location': location, 'URL': earthquake_url})
    
print(earthquake_list)