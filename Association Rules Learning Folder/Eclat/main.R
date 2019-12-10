## importing the dataset 
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
## importing the dataset in a transaction format (you need to install arules package first)
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

## visualizing the item frequencies
itemFrequencyPlot(dataset, topN = 50)

## 
#install.packages('arules')
library(arules)

## Training Apriori algorithm on dataset
rules = eclat(dataset, parameter = list(support = 0.004 , minlen = 2))

# visualization 
inspect(sort(rules, by = 'support')[1:10])