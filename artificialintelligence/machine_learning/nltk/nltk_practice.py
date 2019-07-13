from nltk import word_tokenize, pos_tag, ne_chunk
sentence = "Mark and John are working at Google. Ilanchezhian is testing his name"
print(ne_chunk(pos_tag(word_tokenize(sentence))))