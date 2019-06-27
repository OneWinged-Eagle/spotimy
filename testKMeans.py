from matplotlib import pyplot as plt
import numpy as np

from KMeans import KMeans

X = np.random.rand(50, 2)

for K in range(1, 6):
	km = KMeans(X, K)
	km.run()

	colors = ["r", "g", "b", "k", "c"]
	plt.scatter(km.centroids[:, 0], km.centroids[:, 1], 130, marker="x")

	for i in range(km.m):
		plt.scatter(X[i, 0], X[i, 1], 30, color=colors[km.idx[i]])

	plt.show()
