import simplejson as json 

data = json.load(open('bird_cloudman.json'))

birds = data['birds']



geojson = {
    "type": "FeatureCollection",
    "features": [
    {
        "type": "Feature",
        "geometry" : {
            "type": "Point",
            "coordinates": [i['location']['longitude'], i['location']['latitude']],
            },
        "properties" : i,
     } for i in birds]
}

print(geojson)