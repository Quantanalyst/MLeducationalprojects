# K-fold Cross Validation

Cross-validation is a **resampling** procedure used to evaluate ML models for different purposes. For example, when you have a limited data sample and you can not afford to separate a portion of it as your test set, you can use k-fold CV. The other example is when you want to make sure that you don't have any overfitting. 
The procedure has a single parameter called k that refers to the number of groups that a given data sample is to be split into. It is a popular method because it is simple to understand and because it generally results in a less biased or less optimistic estimate of the model skill than other methods, such as a simple train/test split.

Why using K-Fold CV is a better approach compared to the regualr train/test split? 
typically, the model performance is assessed by fitting the model to the training set and checking it on the test set. But, using test set for model selection has this risk that we might pick a model that is overfitted to the test dataset. In order to remove this risk, we separate the test set from the process of model selection. For model selection, we break the training data into k parts and using one part for test and k-1 parts for the training (this will be done k times and each time we use a different fold for the test and in the end we use the average of the metrics to evaluate the model performance). This way, the model selection process is isolated from the test dataset. When the model selection is finalized, then we can use the test for ultimate model performance assessment. 


The general procedure is as follows:
    1. Shuffle the dataset randomly.
    2. Split the dataset into k groups
    3. For each unique group:
        1. Take the group as a hold out or test data set
        2. Take the remaining groups as a training data set
        3. Fit a model on the training set and evaluate it on the test set
        4. Retain the evaluation score and discard the model
    4. Summarize the skill of the model using the sample of model evaluation scores
