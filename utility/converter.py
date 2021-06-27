# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:03:39 2019
Module for converting JSON data into GeoJSON

@author: Ali
"""


from sys import argv
from os.path import exists
import simplejson as json 


def(json_file:str):

    """Create GeoJSON formatted entry for each record in the json_file and write the result to output file."""

    
    data = json.load(open(json_file))

    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "Point",
                "coordinates": [d["long"], d["lat"]],
                },
            "properties" : d,
         } for d in data]
    }

    output = open("2018_potholes.json", 'w')
    json.dump(geojson, output)
