import json
import spotipy
import spotipy.util as util
from time import perf_counter

import config

with open("json/artists.json") as json_file:
    artists = json.load(json_file)

try:
    token = util.prompt_for_user_token(
        config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    sp = spotipy.Spotify(token)
except:
    print("Token is not accesible for " + config.username)


def retrieve_albums():
    albums = []
    for artistId in [artist["id"] for artist in artists]:
        offset = 0
        while True:
            items = sp.artist_albums(
                artistId, "album,single", limit=50, offset=offset)["items"]
            if len(items) == 0:
                break
            offset += 50
            albums.extend(items)
    return albums


print("Start retrieving albums...")
startTime = perf_counter()

albums = retrieve_albums()

elapsed = perf_counter() - startTime
print(f"Retrieved {len(albums)} albums in {elapsed:.2f}s.")

with open("json/albums.json", "w") as outfile:
    json.dump(albums, outfile)
