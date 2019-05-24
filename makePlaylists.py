import json
from random import shuffle
import spotipy
import spotipy.util as util
from time import perf_counter

from chunker import chunker
import config

with open("json/audioFeatures.json") as json_file:
    audioFeatures = json.load(json_file)

with open("json/indexes.json") as json_file:
    indexes = json.load(json_file)

try:
    token = util.prompt_for_user_token(
        config.username, config.scope, config.client_id, config.client_secret, config.redirect_uri)
    sp = spotipy.Spotify(token)
except:
    print("Token is not accesible for " + config.username)

playlistsIds = []
playlists = []
for i in range(max(indexes) + 1):
    playlistsIds.append(sp.user_playlist_create(
        config.username, "Test " + str(i), False)["id"])
    playlist = []
    for n, trackId in enumerate([audioFeature["id"] for audioFeature in audioFeatures]):
        if indexes[n] == i:
            playlist.append(trackId)
    shuffle(playlist)
    playlists.append(playlist)

for i, playlistId in enumerate(playlistsIds):
    print(f"Start adding tracks to playlist \"Test {i}\"...")
    startTime = perf_counter()
    for tracks in chunker(playlists[i], 100):
        sp.user_playlist_add_tracks(config.username, playlistId, tracks)
    elapsed = perf_counter() - startTime
    print(f"Added {len(playlists[i])} tracks to playlist \"Test {i}\" in {elapsed:.2f}s.")
