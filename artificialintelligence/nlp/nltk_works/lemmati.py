'''
One major difference with stemming is that lemmatize takes a part of speech parameter, “pos” If not supplied, the
default is “noun.”
'''

import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun. studies"
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)

sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    # print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))
    '''
    In the above output, you must be wondering that no actual root form has been given for any word, this is because
     they are given without context. You need to provide the context in which you want to lemmatize that is the parts-of-speech (POS).
     This is done by giving the value for pos parameter in wordnet_lemmatizer.lemmatize
    '''
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word, pos='v')))
print(wordnet_lemmatizer.lemmatize("referral", pos='v'))

# a denotes adjective in "pos"
print("better :", wordnet_lemmatizer.lemmatize("better"))
print("better :", wordnet_lemmatizer.lemmatize("better", pos ="a"))