import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

batch_size = 45
centers = [[1,1],[-1,-1],[1,-1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=3000, cneters=centers, cluster_std=0.7)

import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0

from sklearn.cluster import MiniBatchKMeans

mdk = MiniBatchKMeans(
    init = "k-means++",
    n_clusters = n_clusters,
    n_init = 10,
    max_no_improvement = 10,
    verbose=0,
)
t0 = time.time()
mdk.fit(X)
t_minibatch = time.time() - t0
