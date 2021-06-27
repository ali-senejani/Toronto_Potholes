"""
This module contains utility functions to count pothole frequency for each month and region in the city of Toronto
"""


import json
from collections import Counter
import matplotlib.pyplot as plt



def count_monthly_potholes(monthly_json_file:str):
    
    """Return the pothole count for a specific month of JSON file."""

    
    pothole_list = []

    with open(monthly_json_file) as f:

        j = json.load(f)
    counter = Counter()    
    for d in j:
        for k, v in d.items():
            if k.startswith('service_request_id') and v:
                counter.update([k])
    pothole_list.append(list(counter.values()))

    return pothole_list




def count_regional_potholes(annual_json_file:str):

    """Return a dictionary with count for potholes for each region in Toronto."""
    
    
    etobi_count=0
    yrk_count=0
    eastYrk_count=0
    northYrk_count=0
    frmTo_count=0
    Scar_count=0
    
    with open(annual_json_file) as f:

        j = json.load(f)

    for d in j:
        for key,value in d.items():
            if ', Scarborough' in str(value):
                Scar_count+=1
            elif ', former Toronto' in str(value):
                frmTo_count+=1
            elif ', Etobicoke' in str(value):
                etobi_count+=1
            elif ', East York' in str(value):
                eastYrk_count+=1 
            elif ', North York' in str(value):
                northYrk_count+=1
            elif ', York' in str(value):
                yrk_count+=1

    region_dict = {"Former Toronto":frmTo_count,"North York":northYrk_count,"Scarborough":Scar_count,"Etobicoke":etobi_count,
               "York":yrk_count,"East York":eastYrk_count}

    return region_dict
