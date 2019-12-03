## Random Forest

There are many classification algorithms such as logistic regression, SVM, naive Bayes classifier, and decision trees. But near the top of the classifier hierarchy is the Random Forest.

The **random forest** is a classification algorithm consisting of many decisions trees. It uses 1. **bagging** and 2. **feature randomness** when building each individual tree to try to create an **uncorrelated** forest of trees whose prediction by committee is more accurate than that of any individual tree.

What is needed for the algorithm to make accurate predictions?
* Features must have at least some predictive power.
  * After all, if we put garbage in then we will get garbage out.
* The trees of the forest and more importantly their predictions need to be **uncorrelated** (or at least have low correlations with each other). 
  * While feature randomness tries to engineer low correlations, the selected features and the chosen hyper-parameters will impact the ultimate correlations as well.
