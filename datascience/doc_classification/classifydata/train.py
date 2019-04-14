import numpy as np
from sklearn.datasets import load_files

from datascience.doc_classification.classifydata.Helper import Test

DATA_DIR = "./dataset_5classes/"

data = load_files(DATA_DIR, encoding="utf-8", decode_error="replace")
print("the classes are",data.target_names)
metadata = np.unique(data.target, return_counts=True)

labels=metadata[0]
count=metadata[1]
names=data.target_names
print(dict(zip(names,count)))
for i in range(len(labels)):
    print(labels[i],names[i],labels[i])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)
print("X_test.shape=",len(X_test))
print("Y_test.shape=",y_test.shape)
print("X_train.shape=",len(X_train))
print("y_train.shape=",y_train.shape)
check=dict(zip(X_train,y_train))
print(list(t[:80] for t in X_train[:10]))

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english", max_features=1000, decode_error="ignore")
vectorizer.fit(X_train)
keywords=vectorizer.get_feature_names()
print("keywords=",keywords)
print("keywords size=",len(keywords))
X_train_vectorized = vectorizer.transform(X_train)

#naivebayes
from sklearn.naive_bayes import MultinomialNB
cls = MultinomialNB()
cls.fit(vectorizer.transform(X_train), y_train)

print("type(X_test)=",type(X_test))
print("type(vectorizer.transform(X_test))=",type(vectorizer.transform(X_test)))
testobj=Test()
test_doc=testobj.data_for_a_document()
prediction_for_a_doc=cls.predict(vectorizer.transform(test_doc))


from sklearn.metrics import classification_report, accuracy_score
y_pred = cls.predict(vectorizer.transform(X_test))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import cross_val_score

# start with the classic
# with either pure counts or tfidf features
sgd = Pipeline([
    ("count vectorizer", CountVectorizer(stop_words="english", max_features=3000)),
    ("sgd", SGDClassifier(loss="modified_huber"))
])
sgd_tfidf = Pipeline([
    ("tfidf_vectorizer", TfidfVectorizer(stop_words="english", max_features=3000)),
    ("sgd", SGDClassifier(loss="modified_huber"))
])

svc = Pipeline([
    ("count_vectorizer", CountVectorizer(stop_words="english", max_features=3000)),
    ("linear svc", SVC(kernel="linear"))
])
svc_tfidf = Pipeline([
    ("tfidf_vectorizer", TfidfVectorizer(stop_words="english", max_features=3000)),
    ("linear svc", SVC(kernel="linear"))
])

all_models = [
    ("sgd", sgd),
    ("sgd_tfidf", sgd_tfidf),
    ("svc", svc),
    ("svc_tfidf", svc_tfidf),
]

unsorted_scores = [(name, cross_val_score(model, X_train, y_train, cv=2).mean()) for name, model in all_models]
scores = sorted(unsorted_scores, key=lambda x: -x[1])
print(scores)