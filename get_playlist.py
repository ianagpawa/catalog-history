import sys
import os
import requests
import json
from time import gmtime, strftime

from helper_functions import get_playlist_name, create_folders

timestamp = strftime("%Y%b%d-%H%M%S", gmtime())

playlist_number = sys.argv[1]
playlist_name = get_playlist_name(int(playlist_number))
playlist_url = "http://ec2-34-201-35-166.compute-1.amazonaws.com/playlist/%s/songs/JSON" % playlist_number


print "Getting JSON"
r = requests.get(playlist_url)
playlist_json = r.json()
playlist_decoded = json.dumps(playlist_json)
print "Received JSON"

folder_location = "archive/playlists/%s-%s" % (playlist_number, playlist_name)
# if not os.path.exists(folder_location):
#     print "Creating %s folder" % folder_location
#     os.mkdir(folder_location)
create_folders(file_location)
#
# file_location = "%s/%s.json" % (folder_location, timestamp)
# print "Writing file"
# file = open(file_location, "w")
# file.write(playlist_decoded)
# file.close()
# print "Finished. Created '%s'" % file_location
