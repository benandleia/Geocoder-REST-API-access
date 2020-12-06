# Geocoder-REST-API-access
Python script to access REST API functions of BC Gov't Geocoder system. 

This script is designed to allow for http GET requests using the REST API functionality of the BC Government Geocoder database. A number of functions are support through the API, and a further detailed at: 

https://catalogue.data.gov.bc.ca/dataset/bc-address-geocoder-web-service/resource/40d6411e-ab98-4df9-a24e-67f81c45f6fa/view/1d3c42fc-53dc-4aab-ae3b-f4d056cb00e0?bcgovtm=AgriServiceBCWebinarandprogramannouncement1

The functions leveraged in this script include the GET sites/nearest function. This function take a lat/long coordinate and returns the nearest identified fullAddress string, which includes the locality, street name and civic address (i.e. dwelling number). The search range is set at unlimited; multiple record returns are excluded by designed.

A fullAdress record is returned as a JSON object, extracted and converted to a Pandas dataframe. Seperate locality, street name and civic address values are extracted from the complete stream and provide as seperated dataFrame series (i.e. columns).

This data is then converted to, and exported as, a .CSV record.

Without an API key, the Geocoder server will allow up to 523 sequential get request. A developed API Key should allow for up to 1000 request per min. 
