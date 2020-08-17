import pygeoj
testfile = pygeoj.load("test.geojson")
for feature in testfile:
    print feature.geometry.type
    print feature.geometry.coordinates
