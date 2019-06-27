import json
import numpy as np
import pandas as pd

import config
from KMeans import KMeans
from NumpyEncoder import NumpyEncoder

featuresNames = [
    "acousticness", "danceability", "energy", "instrumentalness", "loudness",
    "speechiness", "valence", "tempo"
]

audioFeatures = pd.read_json("json/audioFeatures.json")[featuresNames]

audioFeatures = (audioFeatures - audioFeatures.min()) / \
 (audioFeatures.max() - audioFeatures.min())

X = audioFeatures.values

with open("json/centroids.json") as json_file:
	centroids = json.load(json_file)

km = KMeans(X, config.nb_playlists)
km.centroids = np.array(centroids[config.nb_playlists - 1])
km.run()

print(len(km.idx))

with open("json/indexes.json", "w") as outfile:
	json.dump(km.idx, outfile, cls=NumpyEncoder)
