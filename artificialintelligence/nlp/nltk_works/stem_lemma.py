from nltk import SnowballStemmer, WordNetLemmatizer


<<<<<<< HEAD
document = ["referral", 'studies', "patient's", "patients"]
=======
document = ["referral", 'studies']
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
stemmer = SnowballStemmer('english')
document = [stemmer.stem(WordNetLemmatizer().lemmatize(word, pos='v')) for word in document if
                            len(word) > 3]
print(document)