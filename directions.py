import requests

lat = 44.038966
long =-123.087558
state = "or"
key = "bf20a5bb85774b0c9e9b7b319c92040f"

origen = "http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?lat=" + str(lat) + "&lon=" + str(long) + "&state=" + str(state) + "&apikey=" + key + "&format=json&notStore=false&version=4.10"

answer = ""
response = requests.get(origen).json()
address = response['StreetAddresses'][0]['StreetAddress']

#remove the addres number, although if the street has a number it will delete it too. Needs improvement.
# for i in address:
#     if i not in "0123456789":
#         answer += i


print(address)
