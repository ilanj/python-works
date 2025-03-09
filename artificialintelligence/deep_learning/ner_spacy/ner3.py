"""python3 -m spacy download en"""

import pprint

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(
    "When Sebastian Thrun started working on self-driving cars at Google "
    "in 2007, few people outside of the company took him seriously."
)

my_dict = {}
for token in doc:
    while token.head != token:
        my_dict[token] = token.dep_
        token = token.head

pprint.pprint(my_dict)
