## Natural Language Processing

# importing the dataset
dataset_original = read.csv('Restaurant_Reviews.tsv', sep = '\t', quote = '', stringsAsFactors = FALSE)

# cleaning the text
# install.packages('tm')
# install.packages('SnowballC')
library(tm)
library(SnowballC)

corpus = VCorpus(VectorSource(dataset_original$Review))
# check the first entry
as.character(corpus[[1]])

corpus = tm_map(corpus, content_transformer(tolower))
# check if tolower function is performed correctly
as.character(corpus[[1]])

corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
## removing stop words
corpus = tm_map(corpus, removeWords, stopwords())
## stemming
corpus = tm_map(corpus, stemDocument)
## removing extra spaces
corpus = tm_map(corpus, stripWhitespace)

## creating a Bag of Words
dtm = DocumentTermMatrix(corpus)
## removing two percent of non-frequent terms
dtm = removeSparseTerms(dtm, 0.999)


## Applying classification - Random Forest
dataset = as.data.frame(as.matrix(dtm))
dataset$Liked = dataset_original$Liked

# Encoding the target feature as factor
dataset$Liked = factor(dataset$Liked, levels = c(0, 1))

library(caTools)
set.seed(123)
split = sample.split(dataset$Liked, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
#training_set[-3] = scale(training_set[-3])
#test_set[-3] = scale(test_set[-3])

# Fitting Random Forest Classification to the Training set
# install.packages('randomForest')
library(randomForest)
set.seed(123)
classifier = randomForest(x = training_set[-692],
                          y = training_set$Liked,
                          ntree = 10)

# Predicting the Test set results
y_pred = predict(classifier, newdata = test_set[-692])

# Making the Confusion Matrix
cm = table(test_set[, 692], y_pred)

