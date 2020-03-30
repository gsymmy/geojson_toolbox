import simplejson as json 

data = json.load(open('bird_cloudman.json'))

birds = data['birds']



geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "properties" : {},
        "geometry" : {
            "type": "Point",
            "coordinates": [i['location']['longitude'], i['location']['latitude']],
            }
     } for i in birds]
}

output = open('output.json', 'w')
json.dump(geojson, output)

print(geojson)