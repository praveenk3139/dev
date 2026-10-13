import pandas as pd
import folium
from bokeh.plotting import figure, show

# 1. Load data
df = pd.read_csv(r'D:\ARCHANA\dxv\LAB\DXV\geographic.csv')

# 2. Bokeh plot with hover tooltips
tooltips = [("Info", "@Info"), ("Latitude", "@Latitude"), ("Longitude", "@Longitude")]
p = figure(width=800, height=400, tooltips=tooltips)
p.circle('Longitude', 'Latitude', size=10, color='orange', source=df)
show(p)

# 3. Folium map
center = [df['Latitude'].mean(), df['Longitude'].mean()]
m = folium.Map(location=center, zoom_start=10)

for _, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Info']).add_to(m)

m.save('map.html')
