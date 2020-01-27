## T-SNE ( t-Distributed Stochastic Neighbour Embedding )

The t-SNE method has become widely popular ever since it was introduced by van der Maaten and Hinton in 2008. Unlike the linear PCA and LDA, t-SNE is a non-linear, probabilistic dimensionality reduction method. Therefore instead of looking at directions/axes which maximise information or class separation, T-SNE aims to convert the Euclidean distances between points into conditional probabilities. A Student-t distribution is then applied on these probabilities which serve as metrics to calculate the similarity between one datapoint to another. 

please do check the original out [here](http://www.cs.toronto.edu/~hinton/absps/tsne.pdf)
