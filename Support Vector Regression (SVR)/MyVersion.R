


### read the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]



### install e1071 package
# install.packages('e1071')
library(e1071)

regressor = svm(formula = Salary ~.,
                  data = dataset, 
                  kernel = 'radial',
                  type = 'eps-regression')


### see the prediction for an employee with level 6 and 2 years of experience (Level = 6.5)

y_pred = predict(regressor,data.frame(Level = 6.5))


### visualization
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, dataset)), color = 'blue') + 
  ggtitle('Salary vs. Level') +
  xlab('Level') +
  ylab('Salary($)')