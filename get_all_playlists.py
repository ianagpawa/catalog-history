import sys
import requests
import json

playlists_url = "http://ec2-34-201-35-166.compute-1.amazonaws.com/playlists/JSON/"

r = requests.get(playlists_url)
playlists_json = r.json()
playlists_decoded = json.dumps(playlists_json)

file = open("test.txt", "w")
file.write(playlists_decoded)
file.close()
