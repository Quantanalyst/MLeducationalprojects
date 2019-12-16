## Linear Discriminant Analysis (LDA)

LDA is very similar to PCA. It is mostly used for dimensionality reduction. However, there are major differences between the two.For example, in LDA, we are also interested in axis that maximize the separation between multiple classes. 

The goal of LDA is to project a feature space ( n-D sample) onto a small subspace k (k < n) while maintaining the class-dicriminatory information. In other words, from the n independent variables of the dataset, LDA extracts p <= n new independent variables that separate the most the classes of the dependent variable. 

Both PCA and LDA are linear transformation techniques used for dimensional reduction. PCA is described as **unsupervised** but LDA is **supervised** because of the relation to the dependent variable. 

Below is the visual difference b/w LDA and PCA. As you see in the LDA case, the projection that captures the maximum variation is not a good axis. 

![LDA vs. PCA](LDAvsPCA.png)
