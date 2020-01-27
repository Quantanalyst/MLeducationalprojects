## Dimensionality Reduction on MNIST dataset using big 3

 1. **Principal Component Analysis ( PCA )**  - Unsupervised, linear method
 2. **Linear Discriminant Analysis (LDA)** - Supervised, linear method
 3. **t-distributed Stochastic Neighbour Embedding (t-SNE)** - Nonlinear, probabilistic method

**Curse of Dimensionality & Dimensionality Reduction:**\
The term "Curse of Dimensionality" refers to situations when our good and reliable ML models paralize when dealing with high-dimensional datasets. Dimensioality reduction techniques are essentially transformation methods used for taking the data from a higher-dimensional space to a lower one while keeping most of the relevant information, that would make life a lot easier for our learning methods.

**PCA vs. LDA**\
PCA tries to find eigenvectors that capture the most variations. However, these variations might not capture the inter-class variations and differences. On the other hand, LDA, by knowing the class labels, try to capture the most variations for all classes. So, if we know the class labels, it is definitely better to reduce the dimension with LDA as it would be much more helpful for classification purposes. 


P.S. MNIST((Mixed National Institute of Standards and Technology))
