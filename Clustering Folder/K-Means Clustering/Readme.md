## K-means Clustering

K-means clustering is an unsupervised ML algorithm. 

* Algorithm:\
  step 1: choose the number K of clusters
  step 2: select K points randomly, the centroids (not necessarily from your dataset)
  step 3: assign each data point to the closest centroid → that forms K clusters
  step 4: compute and place the new centroid of each cluster
  step 5: reassign each data point to the new closest centroid. If any reassignment took place, go to step 4, otherwise, go to FIN(Your model is ready). 

* Random Initialization Trap:\
Incorrect choice of centroids lead to suboptimal clustering. To avoid such a trap, K-means++ algorithm is developed that tries to assign the initial centroids as far as possible. This algorithm has been embedded inside different K-means algorithms. In Scikit-Learn library, the parameter is "init" which must be set to "k-means++". \
$ from sklearn.cluster import KMeans\
$ cluster = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10)

* How to choose the optimal number of clusters?\
The most popular method is Elbow method, which uses Within Cluster Sum of Squares (WCSS) to determine the optimal number of clusters. 
