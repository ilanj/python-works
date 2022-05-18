import nltk
from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
root_word = word_stemmer.stem('walker')
print(root_word)
