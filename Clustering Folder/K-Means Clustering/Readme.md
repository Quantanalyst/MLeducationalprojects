## K-means Clustering

K-means clustering is an unsupervised ML algorithm. 

* Algorithm: 
  step 1: choose the number K of clusters
  step 2: select K points randomly, the centroids (not necessarily from your dataset)
  step 3: assign each data point to the closest centroid → that forms K clusters
  step 4: compute and place the new centroid of each cluster
  step 5: reassign each data point to the new closest centroid. If any reassignment took place, go to step 4, otherwise, go to FIN(Your model is ready). 

* Random Initialization Trap: 
To avoid this trap, use K-means++ algorithm

* How to choose the optimal number of clusters?
The most popular method is Elbow method, which uses Within Cluster Sum of Squares (WCSS) to determine the optimal number of clusters. 
