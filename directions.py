import requests

lat = 44.028804
long = -123.080435
state = "or"
key = "bf20a5bb85774b0c9e9b7b319c92040f"

origen = "http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?lat=" + str(lat) + "&lon=" + str(long) + "&state=" + str(state) + "&apikey=" + key + "&format=json&notStore=false&version=4.10"

answer = ""
response = requests.get(origen).json()
# result = response
address = response['StreetAddresses'][0]['StreetAddress']

for i in address:
    if i not in "0123456789":
        answer += i

print(answer)
