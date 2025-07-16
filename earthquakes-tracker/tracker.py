import requests as rq
import pandas as pd
from operator import itemgetter
import json
import folium

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
        detail_url = properties['detail']

        # move this to make request to only the top ten results for efficiency
        details_req = rq.get(detail_url)
        details = details_req.json()
        latitude = details['properties']['products']['origin'][0]['properties']['latitude']
        longitude = details['properties']['products']['origin'][0]['properties']['longitude']

        earthquake_list.append({'Magnitude': str(magnitude), 'Location': location, 'URL': earthquake_url, 'Coordinates': (latitude, longitude)})

sorted_earthquake_list = sorted(earthquake_list, key=itemgetter('Magnitude'), reverse=True)
top_10 = sorted_earthquake_list[:10]

df = pd.DataFrame(top_10)
df.index += 1

print(f"Top 10 strongest earthquakes this week:\n{df}")

# Part 2
mapit = None

latlon = [tuple(i['Coordinates']) for i in top_10]
print(latlon)
for coord in latlon:
    mapit = folium.Map(location=[coord[0], coord[1]], zoom_start=6)

mapit.save('map.html')