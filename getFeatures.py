import json
import spotipy
import spotipy.util as util
from time import perf_counter

from chunker import chunker
import config

with open("json/tracks.json") as json_file:
	tracks = json.load(json_file)

try:
	token = util.prompt_for_user_token(config.username, config.scope,
	                                   config.client_id, config.client_secret,
	                                   config.redirect_uri)
	sp = spotipy.Spotify(token)
except:
	print("Token is not accesible for " + config.username)

print("Start retrieving audio features...")
startTime = perf_counter()

audioFeatures = []
for tracksIds in chunker([track["id"] for track in tracks], 50):
	audioFeatures.extend(sp.audio_features(tracksIds))
audioFeatures = list(
    audioFeature for audioFeature in audioFeatures if audioFeature)

elapsed = perf_counter() - startTime
print(f"Retrieved {len(audioFeatures)} audio features in {elapsed:.2f}s.")

with open("json/audioFeatures.json", "w") as outfile:
	json.dump(audioFeatures, outfile)
