dataset = read.csv('Churn_Modelling.csv')

dataset = dataset[4:14]

dataset[,2] = as.numeric(factor(dataset[,2], levels = c('France','Spain','Germany'), labels = c(1,2,3)))
dataset[,3] = as.numeric(factor(dataset[,3], labels = c(1,2)))


## split train/test
set.seed(123)
split = sample.split(dataset$Exited, SplitRatio = 0.8)
training_dataset = subset(dataset, split == TRUE)
test_dataset = subset(dataset, split == FALSE)

## feature scaling
training_dataset[,-11] = scale(training_dataset[,-11])
test_dataset[,-11] = scale(test_dataset[,-11])

## install packages for deep learning h20
install.packages('h2o')
library(h2o)

## Using H2O servers - connecting to an available server by h2o.init
h2o.init(nthreads = -1)

## Fitting the ANN to the training model
classifier = h2o.deeplearning(y = 'Exited',
                              training_frame = as.h2o(training_dataset),
                              activation = 'Rectifier',
                              hidden = c(6,6),
                              epochs = 10,
                              train_samples_per_iteration = -2)

## Predicting the accuracy of the trained model
prob_pred = h2o.predict(classifier, newdata = as.h2o(test_dataset[-11]))
y_pred = (prob_pred>0.5)
y_pred = as.vector(y_pred)

## confusion matrix
cm = table(test_dataset[,11],y_pred)
cm

## disconnecting from H2O servers
h2o.shutdown()
