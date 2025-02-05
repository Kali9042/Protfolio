import folium.map
import phonenumbers
import opencage
import folium
from phonenumbers import geocoder

number=input("enter your phone number (with country code):")
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))


from opencage.geocoder import OpenCageGeocode

key='INSERT YOUR API'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("my_location.html")