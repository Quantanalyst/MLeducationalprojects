## Model Performance Evaluation methods

There are many ways to assess the performance of different ML algorithms. In this section, some of them are briefly explained. 

Classification methods:
Below are methods used to evaluate the performance of classification methods.
* CAP curve (Cumulative Accuracy Profile)
  * The CAP Curve tries to analyse how to effectively identify all data points of a given class using minimum number of tries.
  * reading source: [Machine Learning Classifier evaluation using ROC and CAP Curves](https://towardsdatascience.com/machine-learning-classifier-evaluation-using-roc-and-cap-curves-7db60fe6b716)
* ROC curve (Receiver Operating Characteristics)
  * The True Positive Rate (TPR) is plot against False Positive Rate (FPR) for the probabilities of the classifier predictions. Then, the area under the plot is calculated.
* Precision and Recall metrics




## Model Selection 


Some rule of thumb:
  * Logistic Regression or Naive Bayes when you need to rank your predictions by their probability. For example if you want to rank your customers from the highest probability that they buy a certain product, to the lowest probability (to target your marketing campaigns). Then use Logistic Regression if your problem is linear, and Naive Bayes if your problem is non linear.
  * SVM when you want to predict to which segment your customers belong to. Segments can be any kind of segments, for example some market segments you identified earlier with clustering.
  * Decision Tree when you want to have clear interpretation of your model results,
  * Random Forest when you are just looking for high performance with less need for interpretation. 
