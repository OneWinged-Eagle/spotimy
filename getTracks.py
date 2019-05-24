import json
import spotipy
import spotipy.util as util
from time import perf_counter

import config

with open("json/albums.json") as json_file:
    albums = json.load(json_file)

try:
    token = util.prompt_for_user_token(
        config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    sp = spotipy.Spotify(token)
except:
    print("Token is not accesible for " + config.username)


def retrieve_tracks():
    tracks = []
    for albumId in [album["id"] for album in albums]:
        offset = 0
        while True:
            items = sp.album_tracks(
                albumId, limit=50, offset=offset)["items"]
            if len(items) == 0:
                break
            offset += 50
            tracks.extend(items)
    return tracks


print("Start retrieving tracks...")
startTime = perf_counter()

tracks = retrieve_tracks()

elapsed = perf_counter() - startTime
print(f"Retrieved {len(tracks)} tracks in {elapsed:.2f}s.")

uniqueTracks = list(
    {(track["name"].lower(), track["artists"][0]["id"]): track for track in tracks}.values())

print(f"Retrieved {len(uniqueTracks)} (hopefully unique) tracks.")

with open("json/tracks.json", "w") as outfile:
    json.dump(uniqueTracks, outfile)
