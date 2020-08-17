import json
with open(path) as f:
    data = json.load(f)
for feature in data['features']:
    print(feature['properties'])
