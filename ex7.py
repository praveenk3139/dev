import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# 1. Create DataFrame
df = pd.DataFrame({
    'city': ['Berlin', 'Paris', 'Munich'],
    'latitude': [52.52, 48.86, 48.14],
    'longitude': [13.41, 2.35, 11.58]
})

# 2. Convert to GeoDataFrame using points_from_xy
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")

# 3. Plot on base map
ax = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')).plot(color='white', edgecolor='black')
gdf.plot(ax=ax, color='red', markersize=20)
plt.show()
