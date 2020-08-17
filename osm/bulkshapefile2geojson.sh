for filename in ./*.shp; do mkdir -p geojson; ogr2ogr -f "GeoJSON" "./geojson/$filename.geojson" "$filename";done

#Install gdal if you get a ogr2ogr command not found error: https://gdal.org/download.html
