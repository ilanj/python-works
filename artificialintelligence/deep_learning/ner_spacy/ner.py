import os

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Mark and John are working at Google. Ilanchezhian is testing his name")
rootdir = "/home/ila/Documents/5db9961d00c8f8000168950f/text/"
filepaths = os.listdir(rootdir)
for each in filepaths:
    path = rootdir + each
with open(path) as fptr:
    text = fptr.read()
doc = nlp(text)
for token in doc:
    # print(token.text, token.pos_, token.dep)
    if token.pos_ == "PROPN":
        print(token.text, token.pos_, token.dep)
