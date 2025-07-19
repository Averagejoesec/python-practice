import requests as rq
import pandas as pd
from operator import itemgetter
import json
import folium

url = rq.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")

json_response = json.dumps((url.json()), indent=2)

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
        coordinates = earthquake['geometry']['coordinates'][:-1]

        earthquake_list.append({'Magnitude': str(magnitude), 'Location': location, 'URL': earthquake_url, 'Coordinates': coordinates})

sorted_earthquake_list = sorted(earthquake_list, key=itemgetter('Magnitude'), reverse=True)
top_10 = sorted_earthquake_list[:10]
df = pd.DataFrame(top_10)
df.index += 1

print(f"Top 10 strongest earthquakes this week:\n{df}")


# Part 2
coordinates_list = []
for i in sorted_earthquake_list:
    lat_long = i['Coordinates']
    coordinates_list.append(lat_long)

mapit = folium.Map(location=[45.523, -122.675], zoom_start=2,)
for coord in coordinates_list:
    folium.Marker(location=[coord[0], coord[1]],  fill_color='#43d9de', radius=8).add_to(mapit)

mapit.save('earthquakes-tracker/map.html')