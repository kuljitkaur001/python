import phonenumbers
from phonenumbers import geocoder as phone_geocoder
from phonenumbers import carrier
from mynum import number
from opencage.geocoder import OpenCageGeocode
import folium

# OpenCage API key
key = "ef415e75f31742a28d7e44f06e94c3d0"

# Parse number with country
parsed_number = phonenumbers.parse(number, "IN")

# Get location (circle-level / state-level only)
number_location = phone_geocoder.description_for_number(parsed_number, "en")
print(number_location)

# Get carrier
print(carrier.name_for_number(parsed_number, "en"))

# OpenCage geocoding (location name → lat/lng)
opencage = OpenCageGeocode(key)
query = f"{number_location}, India"
results = opencage.geocode(query)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print(lat, lng)

# Create map
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)

map_location.save("mylocation.html")
