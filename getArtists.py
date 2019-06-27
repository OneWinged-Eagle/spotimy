from json import dump
import spotipy
import spotipy.util as util
from time import perf_counter

import config

try:
	token = util.prompt_for_user_token(config.username, config.scope,
	                                   config.client_id, config.client_secret,
	                                   config.redirect_uri)
	sp = spotipy.Spotify(token)
except:
	print("Token is not accesible for " + config.username)


def retrieve_artists():
	artists = []
	lastArtistId = None
	while True:
		items = sp.current_user_followed_artists(50,
		                                         lastArtistId)["artists"]["items"]
		if len(items) == 0:
			break
		lastArtistId = items[-1]["id"]
		artists.extend(items)
	return artists


print("Start retrieving artists...")
startTime = perf_counter()

artists = retrieve_artists()

elapsed = perf_counter() - startTime
print(f"Retrieved {len(artists)} artists in {elapsed:.2f}s.")

with open("json/artists.json", "w") as outfile:
	dump(artists, outfile)
