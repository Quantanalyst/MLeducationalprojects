## Regularization 

In machine learning, **regularization** is typically employed to prevent **overfitting**. Regularization can be described as a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. In other words, this technique discourages learning a more complex or flexible model to avoid the risk of overfitting.

OLS seeks to minimize residual sum of squares or RSS (a.k.a. loss function). If there is noise in the training data, then the estimated coefficients won’t generalize well to the future data. This is where regularization comes in and shrinks or regularizes these learned estimates towards zero. In other words, for any new feature, there would be an entry fee, if the reward of improvement is not greater than the cost of entry, then that feature would be discarded by the algorithm. 



There are three methods for regularization: 
* Ridge

  ![Ridge Equation](Ridge_Equation.png)
  
  Above equation shows ridge regression, where the RSS is modified by adding the shrinkage quantity. Now, the coefficients are estimated by minimizing this function. Here, λ is the tuning parameter that decides how much we want to penalize the flexibility of our model.\
  When λ = 0, the penalty term has no eﬀect, and the estimates produced by ridge regression will be equal to least squares. However, as λ→∞, the impact of the shrinkage penalty grows, and the ridge regression coeﬃcient estimates will approach zero. As can be seen, selecting a good value of λ is critical. Cross validation comes in handy for this purpose. The coefficient estimates produced by this method are also known as the L2 norm.
* Lasso

  ![Ridge Equation](Lasso_Equation.png)
  
Lasso is another variation, in which the above function is minimized. Its clear that this variation differs from ridge regression only in penalizing the high coefficients. It uses |βj|(modulus)instead of squares of β, as its penalty. In statistics, this is known as the L1 norm. 

* Elastic Net
  * TBD
  
**What does Regularization achieve?**
A standard OLS model tends to have some variance in it. Regularization, significantly reduces the variance of the model, without substantial increase in its bias. So the tuning parameter λ, used in the regularization techniques described above, controls the impact on bias and variance. As the value of λ rises, it reduces the value of coefficients and thus reducing the variance. This increase in λ is beneficial to a certain point (reducing the variance(hence avoiding overfitting), without loosing any important properties in the data), but after certain value, the model starts loosing important properties, giving rise to bias in the model and thus underfitting. Therefore, the value of λ should be carefully selected.










P.S. Another way of avoiding overfitting is using cross validation, that helps in estimating the error over test set, and in deciding what parameters work best for your model.
