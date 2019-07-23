import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Mark and John are working at Google. Ilanchezhian is testing his name")
for token in doc:
    print(token.text, token.pos_, token.dep)
    