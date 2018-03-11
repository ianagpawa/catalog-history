import json

playlists = json.loads(
    open('./archive/playlists/2018Mar11-004714.json', 'r').read())['Playlists']

def get_playlist_name(n):
    for playlist in playlists:
        if playlist["id"] == n:
            return playlist["name"]
