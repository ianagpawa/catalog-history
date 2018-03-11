import json
import os

playlists = json.loads(
    open('./archive/all_playlists/2018Mar11-150923.json', 'r').read())['Playlists']

def get_playlist_name(n):
    for playlist in playlists:
        if playlist["id"] == n:
            return playlist["name"]

def create_folders(file_location):
    folders = file_location.split('/')
    current = ""
    for folder in folders:
        if folder != "":
            current += folder + "/"
            next if (os.path.exists(current)) else os.mkdir(current)

    print "Done creating folders"
