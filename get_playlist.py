import sys
import os
import requests
import json
from time import gmtime, strftime

# timestamp = strftime("%Y%b%d-%H%M%S", gmtime())
#
playlist_number = sys.argv[1]
playlists_url = "http://ec2-34-201-35-166.compute-1.amazonaws.com/playlist/%s/songs/JSON" % playlist_number


print "Getting JSON"
r = requests.get(playlists_url)
playlists_json = r.json()
playlists_decoded = json.dumps(playlists_json)
print "Received JSON"

# folder_location = "archive/1"
# if not os.path.exists(folder_location):
#     print "Creating %s folder" % folder_location
#     os.mkdir(folder_location)
#
# file_location = "%s/%s.txt" % (folder_location, timestamp)
# print "Writing file"
# file = open(file_location, "w")
# file.write(playlists_decoded)
# file.close()
# print "Finished. Created '%s'" % file_location
