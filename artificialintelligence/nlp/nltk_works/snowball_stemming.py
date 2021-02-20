'''
Imput: list of words
Output: caring ----> (True, True)----->care  (originalWord --->(if original word in dict, stemmed word in dict) ----> stemmed word)
'''
import nltk
from nltk.stem.snowball import SnowballStemmer

import enchant
d = enchant.Dict("en_US")

def check_in_dict(word, x):
    # d = enchant.Dict("en_US")
    status_original = d.check(word)
    status_stem = d.check(word)
    return status_original, status_stem

# the stemmer requires a language parameter
snow_stemmer = SnowballStemmer(language='english')

# list of tokenized words
words = ['caring', 'cared', 'university', 'fairly', 'easily', 'singing',
         'sings', 'sung', 'singer', 'sportingly', 'going', "pleaded", 'chairs', 'went', 'gone', 'was']

# stem's of each word
stem_words = []
dict_words = []
for w in words:
    x = snow_stemmer.stem(w)
    stem_words.append(x)
    status = str(check_in_dict(w,x))
    dict_words.append(status)


# print stemming results
for e1, e2, e3 in zip(words, dict_words, stem_words):
    print(e1 + ' ----> ' + e2 + '----->'+ e3)

