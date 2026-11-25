import folium

m = folium.Map(location=[13.08, 80.27], zoom_start=5, tiles="Esri.WorldStreetMap")

cities = {
    "Chennai": [13.08, 80.27],
    "Bangalore": [12.97, 77.59],
    "Mumbai": [19.07, 72.87],
    "Delhi": [28.61, 77.20]
}

for city, loc in cities.items():
    folium.Marker(
        loc,
        tooltip=f"{city} | Lat: {loc[0]} | Lon: {loc[1]}"
    ).add_to(m)

m.save("map.html")

import webbrowser
webbrowser.open("map.html")
