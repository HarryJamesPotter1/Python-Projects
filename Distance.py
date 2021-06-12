from geopy.geocoders import Nominatim

from geopy import distance

a = Nominatim(user_agent="Kushal")

Place1 = input("Enter a place: ")
Place2 = input("Enter another place: ")
print("")

Destination1 = a.geocode(Place1)
Destination2 = a.geocode(Place2)

Lat1, Long1 = (Destination1.latitude), (Destination1.longitude)
Lat2, Long2 = (Destination2.latitude), (Destination2.longitude)

Length1 = (Lat1, Long1)
Length2 = (Lat2, Long2)

print("The distance between", Place1, "and", Place2, "is", distance.distance(Length1, Length2))