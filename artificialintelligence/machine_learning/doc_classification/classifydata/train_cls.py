import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_files
import joblib
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import plot_confusion_matrix

DATA_DIR = "dataset_5classes"

data = load_files(DATA_DIR, encoding="utf-8", decode_error="replace")
metadata = np.unique(data.target, return_counts=True)

labels = metadata[0]
count = metadata[1]
class_names = data.target_names

print("cls/name/no_of_docs")
for i in range(len(labels)):
    print(labels[i], class_names[i], count[i])

print("-----------------------------------------------------------------")
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.20, random_state=False
)  # test_size=0.50
print("X_test.shape=", len(X_test))
print("Y_test.shape=", y_test.shape)
print("X_train.shape=", len(X_train))
print("y_train.shape=", y_train.shape)
print("-----------------------------------------------------------------")


# count vectorizer for BOW, just implemented and not used
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
# tfidf -used here
vectorizer = TfidfVectorizer(
    stop_words="english", max_features=2000, decode_error="ignore"
)
vectorizer.fit(X_train)
keywords = vectorizer.get_feature_names()
X_train_vectorized = vectorizer.transform(X_train)
with open("stopwords.txt", "w") as fptr:
    for word in vectorizer.stop_words_:
        fptr.write(word + " ")
    for word in ENGLISH_STOP_WORDS:
        fptr.write(word + " ")
with open("features.txt", "w") as fptr:
    for word in keywords:
        fptr.write(word + " ")

# naivebayes
cls = MultinomialNB(alpha=0.001)
clf = RandomForestClassifier(n_estimators=5)  # ensemble method
cls.fit(vectorizer.transform(X_train), y_train)
joblib.dump(cls, "" + "nb_model.h5")
y_pred = cls.predict(vectorizer.transform(X_test))
print("accuracy with naive bayes = ", accuracy_score(y_test, y_pred))

# svc model
svc_tfidf = Pipeline(
    [
        ("tfidf_vectorizer", TfidfVectorizer(stop_words="english", max_features=3000)),
        ("linear svc", SVC(kernel="linear")),
    ]
)

models = [
    ("svc_tfidf", svc_tfidf),
]
svc_score = [
    (name, cross_val_score(model, X_train, y_train, cv=2).mean())
    for name, model in models
]
scores = sorted(svc_score, key=lambda x: -x[1])
print("svc accuracy ", scores)


# Plot non-normalized confusion matrix
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(
        cls,
        vectorizer.transform(X_test),
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

plt.show()
plt.savefig("cf.png", format="png")
