# Model Selection Techniques

After we built our Machine Learning models, some questions remained unanswered:
  * How to deal with the bias-variance tradeoff when building a model and evaluating its performance?
  * How to choose the optimal values for the hyperparameters (the parameters that are not learned)?
  * How to find the most appropriate ML model for my business problem?

Some Model Selection techniques:
  * k-Fold Cross Validation
  * Grid Search

Why do we need K-Fold CV? 
typically, the model performance is assessed by fitting the model to the training set and checking it on the test set. But, using test set for model selection has this risk that we might pick a model that is overfitted to the test dataset. In order to remove this risk, we separate the test set from the process of model selection. For model selection, we break the training data into k parts and using one part for test and k-1 parts for the training (this will be done k times and each time we use a different part for the test and in the end we use the average of the metrics). This way, the model selection process is isolated from our test dataset. When the model selection is finalized, then we can use the test for ultimate model performance assessment. 
