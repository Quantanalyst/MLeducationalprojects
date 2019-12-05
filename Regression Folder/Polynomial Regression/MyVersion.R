

dataset = read.csv('Position_Salaries.csv')

## R is 1-indexed
dataset = dataset[2:3]

dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4

regressor = lm(formula = Salary ~ .,
               data = dataset)

summary(regressor)

### visualization by ggplot2
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor,dataset))) +
  ggtitle('Salary vs. Level') +
  xlab('Level') +
  ylab('Salary ($)')