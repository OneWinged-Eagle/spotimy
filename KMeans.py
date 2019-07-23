import numpy as np
from typing import List

class KMeans:
	X: np.ndarray
	K: int
	max_iter: int
	tol: float
	m: int
	n: int
	centroids: List[np.ndarray]
	idx: np.ndarray
	distance: np.ndarray

	def __init__(self, X: np.ndarray, K: int = 8, max_iter: int = 300, tol: float = 1e-4):
		self.X = X
		self.K = K
		self.max_iter = max_iter
		self.tol = tol

		self.m = X.shape[0]
		self.n = X.shape[1]
		self.centroids = X[np.random.choice(self.m, K, False)]
		self.idx = np.zeros(self.m)
		self.distances = np.zeros((self.m, K))

	def run(self):
		for _ in range(self.max_iter):
			# findClosestCentroids
			for k in range(self.K):
				self.distances[:, k] = np.linalg.norm(
				    self.X - self.centroids[k], axis=1)
			self.idx = self.distances.argmin(1)
			# /findClosestCentroids

			previousCentroids = self.centroids.copy()

			# computeCentroids
			for k in range(self.K):
				self.centroids[k] = np.mean(self.X[self.idx == k], 0)
			# /computeCentroids

			if np.linalg.norm(self.centroids - previousCentroids) < self.tol:
				break
