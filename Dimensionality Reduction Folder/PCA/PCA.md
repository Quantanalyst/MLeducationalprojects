## Principal Component Analysis (PCA) 

Algorithm: 
1. Standardize the data
2. Obtain Eigenvectors and Eigenvalues from the covariance matrix or SVD
3. Sort Eigenvalues in descending order and choose the k eigenvectors corresponding to the k largest eigenvalues (k < d)
4. Construct the projection matrix W from the k eigenvectors
5. Transform the original dataset X via W to obtain a k-dimensional feature subspace



