## Random Forest

There are many classification algorithms such as logistic regression, SVM, naive Bayes classifier, and decision trees. But near the top of the classifier hierarchy is the Random Forest.

The **random forest** is a classification algorithm consisting of many decisions trees. It uses 1. **bagging** and 2. **feature randomness** when building each individual tree to try to create an **uncorrelated** forest of trees whose prediction by committee is more accurate than that of any individual tree.

What is needed for the algorithm to make accurate predictions?
* Features must have at least some **predictive power**.
  * After all, if we put garbage in then we will get garbage out.
* The trees of the forest and more importantly their predictions need to be **uncorrelated** (or at least have low correlations with each other). 
  * While feature randomness tries to engineer low correlations, the selected features and the chosen hyper-parameters will impact the ultimate correlations as well.

Techniques employed to ensure that the different trees diversify each other:
It uses the following two methods:
* Bagging (Bootstrap Aggregation)
  * Decisions trees are very sensitive to the data they are trained on — small changes to the training set can result in significantly different tree structures. Random forest takes advantage of this by allowing each individual tree to randomly sample from the dataset with **replacement**, resulting in different trees. This process is known as bagging.
* Feature Randomness
  * In a normal decision tree, when it is time to split a node, we consider every possible feature and pick the one that produces the most separation between the observations in the left node vs. those in the right node. In contrast, each tree in a random forest can pick only from a random subset of features. This forces even more variation amongst the trees in the model and ultimately results in lower correlation across trees and more diversification.
