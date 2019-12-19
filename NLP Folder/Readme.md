## Natural Language Processing (NLP)



Question: What is the _difference_ b/w **lemmatization** and **stemming**?
Lemmatization and Stemming are very similar. However, there is one slight difference that makes them two different things. **Stemming** is the process of reducing _inflection_ in words to their root forms such as mapping a group of words to the same stem _even if the stem itself is not a valid word in the Language_." 
**Lemmatization**, unlike Stemming, reduces the inflected words properly ensuring that the root word belongs to the language. In Lemmatization root word is called Lemma. A lemma is the canonical form, dictionary form, or citation form of a set of words.

Source [Stemming vs. Lemmatization](https://www.datacamp.com/community/tutorials/stemming-lemmatization-python)


Question: What is the difference between **CountVectorizer** and **TfidfVectorizer**?
Both methods try to tokenize a document and they are very similar in nature. The CountVectorizer provides a simple way to both 1. tokenize a collection of text documents and 2. build a vocabulary of known words (fitting part), and also to encode new documents using that vocabulary (transform part). An encoded vector (transformed document) is returned with a length of the entire vocabulary and an integer count for the number of times each word appeared in the document.

One issue with simple counts is that some words like “the” will appear many times and their large counts will not be very meaningful in the encoded vectors.

An alternative is to calculate word frequencies, and by far the most popular method is called **TF-IDF**. This is an acronym than stands for “Term Frequency – Inverse Document” Frequency which are the components of the resulting scores assigned to each word.
  * Term Frequency: This summarizes how often a given word appears within a document.
  * Inverse Document Frequency: This downscales words that appear a lot across documents.
Without going into the math, TF-IDF are word frequency scores that try to highlight words that are more interesting, e.g. frequent in a document but not across documents.

Question: What is N-gram ? 
An n-gram model is a type of probabilistic language model for predicting the next item in such a sequence in the form of a (n − 1)–order Markov model. In other words, it will club N adjacent words in a sentence based upon N.
  * If input is “wireless speakers for tv”:
    * N=1 Unigram- Ouput- “wireless” , “speakers”, “for” , “tv”
    * N=2 Bigram- Ouput- “wireless speakers”, “speakers for” , “for tv”
    * N=3 Trigram - Output- “wireless speakers for” , “speakers for tv”



