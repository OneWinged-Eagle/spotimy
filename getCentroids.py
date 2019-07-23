import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from time import perf_counter

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

centroids = []
wcssArray = []
for K in range(1, config.max_cluster + 1):
	print(f"Start calculating centroids for {K} clusters...")
	startTime = perf_counter()

	km = KMeans(X, K)
	km.run()
	centroids.append(km.centroids)

	wcss = 0
	for k in range(K):
		wcss += np.sum((X[km.idx == k] - km.centroids[k])**2)
	wcssArray.append(wcss)

	elapsed = perf_counter() - startTime
	print(f"Calcuted centroids for {K} clusters in {elapsed:.2f}s.")

plt.plot([K for K in range(1, config.max_cluster + 1)], wcssArray)
plt.xlabel("Number of Clusters")
plt.ylabel("within-cluster sums of squares (WCSS)")
plt.title("Elbow method to determine optimum number of clusters")
plt.show()

with open("json/centroids.json", "w") as outfile:
	json.dump(centroids, outfile, cls=NumpyEncoder)
