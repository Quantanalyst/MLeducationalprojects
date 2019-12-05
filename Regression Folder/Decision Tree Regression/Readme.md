## Decision Tree Regression

A Decision Tree regression can provide a numerical prediction for each observation. The algorithm to select root nodes and decision nodes (from a list of available features) is ID3, which is a top-down greedy search through the space of possible branches with no backtracking.This algorithm seeks to maximize Information Gain by **Standard Deviation Reduction**. 

In summary, A decision tree is built top-down from a root node and involves partitioning the data into subsets that contain instances with similar values (homogenous). e use standard deviation to calculate the homogeneity of a numerical sample. If the numerical sample is completely homogeneous its standard deviation is zero.

Differences b/w Decision Tree Regression and Classification:
* Numerical and Categorical outputs for Regression and Classification, respectively
* Standard Deviation reduction and GINI Impurity reduction as branching techniques for Regression and Classification, respectively
