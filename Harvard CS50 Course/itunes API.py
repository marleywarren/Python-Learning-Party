# python3 "/Users/marleywarren/Dropbox (Rush)/Python Learning Party/Harvard CS50 Course/itunes.py"
import json # comes with the json.dumps fx whiich makes JSON requests more asthetically pleasing
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent= 2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])

