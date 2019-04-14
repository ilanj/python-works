import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"When Sebastian Thrun started working on self-driving cars at Google "
          u"in 2007, few people outside of the company took him seriously.")

dep_labels = []
for token in doc:
    while token.head != token:
        dep_labels.append(token.dep_)
        token = token.head
print(dep_labels)