## Naive Bayes Classifier

Naive Bayes is a simple, yet effective and commonly-used ML classifier. It is a probabilistic classifier using the Maximum A Posteriori decision rule in a Bayesian setting. Naive Bayes classifiers have been especially popular for text classification, and are a traditional solution for problems such as spam detection.

A good reading source: [Introduction to Naive Bayes Classification](https://towardsdatascience.com/introduction-to-naive-bayes-classification-4cffabb1ae54)

Note that there is very little explicit training in Naive Bayes compared to other common classification methods. The only work that must be done before prediction is finding the parameters for the features’ individual probability distributions, which can typically be done quickly and deterministically. This means that Naive Bayes classifiers can perform well even with high-dimensional data points and/or a large number of data points.
