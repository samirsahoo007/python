import geojson
with open(path_to_file) as f:
    gj = geojson.load(f)
features = gj['features'][0]
