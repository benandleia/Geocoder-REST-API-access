# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:05:40 2020

@author: SnowBe
"""

import requests
import pandas as pd

##################################################IMPORT THE WELL DATA #############################################################

start_data = pd.read_csv('/Users/SnowBe/Desktop/well.csv')

geographic = start_data[["longitude", "latitude"]]
 
API_Key = "gpgA7PI51KWq1aillCymxzXlPyg301m1"

data_entries = len(geographic.index)

full_address = []
civic_number = []
street = []
locality = []
long = []
lat = []

for i in range(10):
    resp = requests.get('https://geocoder.api.gov.bc.ca/sites/nearest.json?point=' + str(geographic["longitude"][i]) + '%2C' +
                        str(geographic['latitude'][i]))
    if resp.status_code != 200:
         # This means something went wrong.
         raise Exception('Error Code {}'.format(resp.status_code))
    data = resp.json()
    full_address.append(data["properties"]["fullAddress"])
    civic_number.append(data["properties"]["civicNumber"])
    street.append(data["properties"]["streetName"])
    locality.append(data["properties"]["localityName"])
    long.append(geographic["longitude"][i])
    lat.append( geographic['latitude'][i])
    print("Processing Record {} of {}".format(i, data_entries))
    
#Assemble the dictionary, convert to a data frame

output = {"locality":locality, "full_address": full_address, "civic_number": civic_number, "street_name": street, "latitude": lat, "longitude": long}

output_df = pd.DataFrame(output)    

