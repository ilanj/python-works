import spacy

# nlp = spacy.load("en_core_web_md")
nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Apple and guava are similar. Pasta and hippo aren't.")

apple = doc[0]
mat = doc[2]
pasta = doc[6]
hippo = doc[8]

print("apple <-> mat", apple.similarity(mat))
print("pasta <-> hippo", pasta.similarity(hippo))
print(apple.has_vector, mat.has_vector, pasta.has_vector, hippo.has_vector)