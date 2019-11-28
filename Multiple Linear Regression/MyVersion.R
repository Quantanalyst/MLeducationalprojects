

dataset = read.csv('50_Startups.csv')


### Encoding categorical data --> factor()
dataset$State = factor(dataset$State,
                            levels = c('New York','California','Florida'),
                            labels = c(1,2,3))


### split train/test dataset
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


### Linear Regression
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = training_set)
# regressor = lm(formula = Profit ~ ., data = training_set)  ## alternative version

## note : R is smart enough to not fall into dummy  variable trap. the lm library takes care of dummy 
## variable trap by removing one dummy variable. 

summary(regressor)

## predicting the test set
y_pred = predict(regressor, test_set)


### Building optimal model using Backward Elimination 
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = dataset)
summary(regressor)



### Automatic Backward Elimination 
backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)