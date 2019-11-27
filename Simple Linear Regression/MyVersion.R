# Importing the dataset
dataset = read.csv('Salary_Data.csv')


# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)


## linear regression model 
regressor = lm(formula = Salary ~ YearsExperience, 
              data = training_set)

## to check the regressor info, you can use summary(regressor) command
summary(regressor)

### prediction
y_pred = predict(regressor, newdata = test_set)

## visualization
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary), color = 'red') +
  geom_line (aes(x=training_set$YearsExperience, y=predict(regressor,newdata = training_set)), color = 'blue') +
  ggtitle('Salary vs. Years of Experience (Training Dataset)') +
  xlab('Years of Experience') + 
  ylab('Salary')

ggplot() +
  geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary), color = 'red') +
  geom_line (aes(x=training_set$YearsExperience, y=predict(regressor,newdata = training_set)), color = 'blue') +
  ggtitle('Salary vs. Years of Experience (Test Dataset)') +
  xlab('Years of Experience') + 
  ylab('Salary')
