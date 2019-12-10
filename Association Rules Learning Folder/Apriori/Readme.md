## Apriori Algorithm

Apriori is one form of Association Rule Learning. It is one of the basic form of recommender systems. The algorithm follows the below steps:
step 1: set a minimum support and confidence
step 2: take all the subsets in transactions having higher support than minimum support
step 3: take all the rules of these subsets having higher confidence than minimum confidence
step 4: sort the rules by decreasing lift 


The input of the algorithm is a sparse matrix.
You can improve the performance of associative rules learning by using collaborative filtering, Latent Factor models, and neighborhood model. 

Source: [Complete guide to Association Rules
](https://towardsdatascience.com/association-rules-2-aa9a77241654)
