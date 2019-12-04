## Regularization 

In machine learning, **regularization** is typically employed to prevent **overfitting**. Regularization can be described as a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. In other words, this technique discourages learning a more complex or flexible model to avoid the risk of overfitting.

OLS seeks to minimize residual sum of squares or RSS (a.k.a. loss function). If there is noise in the training data, then the estimated coefficients won’t generalize well to the future data. This is where regularization comes in and shrinks or regularizes these learned estimates towards zero.



There are three methods for regularization: 
* Ridge
* Lasso
* Elastic Net

Regularization applies to loss functions. 










P.S. Another way of avoiding overfitting is using cross validation, that helps in estimating the error over test set, and in deciding what parameters work best for your model.
