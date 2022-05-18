from nltk import SnowballStemmer, WordNetLemmatizer


document = ["referral", 'studies', "patient's", "patients"]
stemmer = SnowballStemmer('english')
document = [stemmer.stem(WordNetLemmatizer().lemmatize(word, pos='v')) for word in document if
                            len(word) > 3]
print(document)