import geopandas as gpd
earthquake = gpd.read_file('earthquake.geojson')
print(earthquake.head())
