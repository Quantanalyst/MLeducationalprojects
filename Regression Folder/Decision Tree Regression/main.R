

dataset = read.csv('Position_Salaries.csv')

dataset = dataset[2:3]

# install.packages('rpart')

library(rpart)


regressor = rpart(formula = Salary ~.,
                  data = dataset,
                  control = rpart.control(minsplit = 1))

summary(regressor)

y_pred = predict(regressor,dataset)

x_grid = seq(min(dataset$Level),max(dataset$Level),0.01)
y_pred = predict(regressor,data.frame(Level = x_grid))

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = x_grid, y=y_pred), color = 'blue') +
  ggtitle('Salary vs. Level') +
  xlab('Level') +
  ylab('Salary')

