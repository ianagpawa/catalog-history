import os
import requests
import json
from time import gmtime, strftime

timestamp = strftime("%Y%b%d-%H%M%S", gmtime())

playlists_url = "http://ec2-34-201-35-166.compute-1.amazonaws.com/playlists/JSON/"

print "Getting JSON"
r = requests.get(playlists_url)
playlists_json = r.json()
playlists_decoded = json.dumps(playlists_json)
r.close()
print "Received JSON"

folder_location = "archive/playlists"
if not os.path.exists(folder_location):
    print "Creating %s folder" % folder_location
    os.mkdir(folder_location)

file_location = "%s/%s.txt" % (folder_location, timestamp)
print "Writing file"
file = open(file_location, "w")
file.write(playlists_decoded)
file.close()
print "Finished. Created '%s'" % file_location
