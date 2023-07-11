import phonenumbers
import opencage
from test import number
import folium

from phonenumbers import geocoder
pep_number = phonenumbers.parse(number)
location = geocoder.description_for_number(pep_number, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
service_provider = carrier.name_for_number(service_pro, "en")
print(service_provider)

from opencage.geocoder import OpenCageGeocode
key = '496645f6b4ef47238b7bb5994f867ed7'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
print(results) 

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('myLocation.html')

