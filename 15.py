import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Create DataFrame
df = pd.DataFrame({
    'city': ['Chennai', 'Coimbatore', 'Madurai'],
    'latitude': [13.08, 11.01, 9.92],
    'longitude': [80.27, 76.95, 78.11]
})

# 2. Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df.longitude, df.latitude),
    crs="EPSG:4326"
)

# 3. Load India Map
india = gpd.read_file("india_states.geojson")

# 4. Plot Map
ax = india.plot(color='white', edgecolor='black')
gdf.plot(ax=ax, color='red', markersize=20)

plt.title("State-wise and District-wise Mapping in India")
plt.show()