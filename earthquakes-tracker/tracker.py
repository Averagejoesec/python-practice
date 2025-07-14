import requests as rq
import pandas as pd
from operator import itemgetter
import json

url = rq.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")

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
        # Remove 'None' magnitude
        if properties['mag'] != None:
            magnitude = properties['mag']
        location = properties['place']
        earthquake_url = properties['url']

        earthquake_list.append({'Magnitude': str(magnitude), 'Location': location, 'URL': earthquake_url})

sorted_earthquake_list = sorted(earthquake_list, key=itemgetter('Magnitude'), reverse=True)

for i in sorted_earthquake_list[:10]:
    print(i)