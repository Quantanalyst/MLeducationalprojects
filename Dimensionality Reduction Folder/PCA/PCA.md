## Principal Component Analysis (PCA) 

In a nutshell, PCA is a linear transformation algorithm that seeks to project the original features of our data onto a smaller set of features ( or subspace ) while still retaining most of the information. To do this the algorithm tries to find the most appropriate directions/angles ( which are the principal components ) that maximise the variance in the new subspace. Why maximise the variance though? 

To answer the question, more context has to be given about the PCA method. One has to understand that the principal components are orthogonal to each other ( think right angle ). As such when generating the covariance matrix ( measure of how related 2 variables are to each other ) in our new subspace, the off-diagonal values of the covariance matrix will be zero and only the diagonals ( or eigenvalues) will be non-zero. It is these diagonal values that represent the *variances* of the principal components that we are talking about or information about the variability of our features. 

Therefore when PCA seeks to maximise this variance, the method is trying to find directions ( principal components ) that contain the largest spread/subset of data points or information ( variance ) relative to all the data points present. For a brilliant and detailed description on this, check out this stackexchange thread: 

[PCA and proportion of variance explained](http://stats.stackexchange.com/a/140579/3277)

Algorithm: 
1. Standardize the data
2. Obtain Eigenvectors and Eigenvalues from the covariance matrix or SVD
3. Sort Eigenvalues in descending order and choose the k eigenvectors corresponding to the k largest eigenvalues (k < d)
4. Construct the projection matrix W from the k eigenvectors
5. Transform the original dataset X via W to obtain a k-dimensional feature subspace



