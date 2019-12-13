## Bag of Words

A very well-known model in NLP is the Bag of Words model. It is a model used to preprocess the texts to classify before fitting the classification algorithms on the observations containing the texts.

Algorithm:\
  * step 1: cleaning the text. cleaning the text consists of the following activities: removing stop words, stemming, lower casing. The whole point of text cleaning is to decrease the size of the final sparse matrix. For example, having a word in two formats, one lower case and one with capital case only adds to the size of the final sparse matrix without adding any value to better understanding the document.\
  * step 2: Tokenization. It is the process of creating a matrix which every column corrosponds to a unique word in the corpus and every row corrosponds to an observation. 
  * step 3: Applying the classification model
