dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]


## library
library(stats)

## hierarchical clustering 
dendogram = hclust(d = dist(X, method = 'euclidean'), method = 'ward.D')
plot(dendogram,
     main = paste('Dendogram'),
     xlab = 'Customers',
     ylab = 'Euclidean Distance')

## fitting hierarchical clustering
hc = hclust(d = dist(X, method = 'euclidean'), method = 'ward.D')
y_hc = cutree(hc,5)

## visualization
library(cluster)

clusplot(X,
         y_hc,
         lines = 0,
         labels = 1,
         shade = TRUE,
         color = TRUE,
         main = paste('Cluster of Customers'),
         xlab = 'Annual Income (k$)',
         ylab = 'Spending Score'
         )