# This code will not be as accurate as you may think as I think it only uses
# The center coordinates of a country to feed into folium which is why the result will
# have a location pinned at the center of a country.
import os
import folium
from dotenv import load_dotenv
from phonenumbers import geocoder as phonenumbers_geocoder, carrier, parse, PhoneNumber
from opencage.geocoder import OpenCageGeocode

load_dotenv()

number: str = input("\n\tPlace your phonenumber with country code (+63123456789): ")

geocoding_api_key: str = os.getenv("KEY")
# You may get your own api key FOR FREE by signing up at https://opencagedata.com/
# And visit their tutorial site to get the api key at the link below
# https://opencagedata.com/tutorials/geocode-in-python

geocoder = OpenCageGeocode(geocoding_api_key)

number_instance: PhoneNumber = parse(number, None)
country_of_origin: str = phonenumbers_geocoder.description_for_number(number_instance, "en")
service_carrier: str = carrier.name_for_number(number_instance, "en")

query =str(country_of_origin)

# returns a search results query
search_results = geocoder.geocode(query)

latitude = search_results[0]['geometry']['lat']
longhitude = search_results[0]['geometry']['lng']

map = folium.Map(location =[latitude, longhitude], zoom_start_= 9)
folium.Marker([latitude , longhitude], popup=country_of_origin).add_to(map)

map.save("phone_location.html")
print("\tPhone location has been saved\n")