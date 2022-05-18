from gensim.utils import simple_preprocess

text = "9 is an example no and is used here and is used here a . EnD FILE Over;"

preprocessed_text = simple_preprocess(text)
print(preprocessed_text)