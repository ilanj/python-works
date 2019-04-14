import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"jhon is from pondicherry, ilanchezhian is from india")
for token in doc:
    print(token.text, token.pos_, token.dep)