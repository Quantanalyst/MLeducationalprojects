
dataset = read.csv('Mall_Customers.csv')
dataset = dataset[4:5]


## library
library(stats)
## using elbow method to find the optimal number of clusters
wcss = vector()
set.seed(6)
for (i in 1:10)
  wcss[i] = sum(kmeans(dataset, i)$withinss)

plot(1:10, wcss, type = "b", main = paste("Clusters of Clients"), xlab = "Number of Clusters", ylab = "WCSS")


## Applying K-means to mall dataset
set.seed(29)
kmeans = kmeans(dataset, 5, iter.max = 300, nstart = 10)

## visualization
# install.packages('cluster')
library(cluster)

clusplot(dataset,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 1,
         plotchar = TRUE,
         span = TRUE,
         main = paste('Clusters of Clients'),
         xlab = 'Annual Income',
         ylab = 'Spending Score'
         )

