import sys
import os
import requests
import json
from time import gmtime, strftime

timestamp = strftime("%Y%b%d-%H%M%S", gmtime())

# playlists_url = "http://ec2-34-201-35-166.compute-1.amazonaws.com/playlists/JSON/"
#
# r = requests.get(playlists_url)
# playlists_json = r.json()
# playlists_decoded = json.dumps(playlists_json)

folder_location = "archive/playlists"
if not os.path.exists(folder_location):
    os.mkdir(folder_location)
file_location = "%s/%s.txt" % (folder_location, timestamp)
# file = open(file_location, "w")
# file.write(playlists_decoded)
# file.close()
