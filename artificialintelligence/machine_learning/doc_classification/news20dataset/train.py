from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

print("categories=",twenty_train.target_names) #prints all the categoris)
print("\n".join(twenty_train.data[0].split("\n")[:3])) #prints first line of the first data file
print("twenty_type=",type(twenty_train))
print("twenty_type.data=",type(twenty_train.data))
# str="abc abcd abcde \n klnjk jnjn jjn"
# print(str.split("\n")[:1])

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print("featurenames",count_vect.get_feature_names())
print(type(count_vect.get_feature_names()))
words=count_vect.get_feature_names()
print("words count = ", len(words))
# print(type("x_train_counts=",type(X_train_counts)))
print("X_train_counts.shape",X_train_counts.shape)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf=count_vect.fit_transform(twenty_train.data)
print(count_vect.get_feature_names())
print(len(count_vect.get_feature_names()))
print(X_train_tfidf.shape)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])#check without stopwords
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

import numpy as np
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
# predicted = text_clf.predict(twenty_test.data)
print("twenty_test_datatype",type(twenty_test.data))
predict_data=twenty_test.data
print(predict_data[0])
predicted = text_clf.predict(predict_data[:])
print("type(predicted)=",type(predicted))
print("predicted=",predicted)
print(np.mean(predicted == twenty_test.target))

from sklearn.linear_model import SGDClassifier
text_clf_svm = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf-svm',
    SGDClassifier(loss='hinge',penalty='l2',alpha=1e-3, n_iter=5, random_state=42)),])#removing stopwords here has same or reduced effect
_ = text_clf_svm.fit(twenty_train.data, twenty_train.target)
predict_data1=twenty_test.data
predicted_svm = text_clf_svm.predict(predict_data1[:])
print("using svm",predicted_svm)
print(np.mean(predicted_svm == twenty_test.target))

# #improved tuning for NB
# from sklearn.model_selection import GridSearchCV
# parameters = {'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),'clf__alpha': (1e-2, 1e-3)}
# gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
# gs_clf = gs_clf.fit(twenty_train.data, twenty_train.target)
# print(gs_clf.best_score_)
# print(gs_clf.best_params_)
#
# #improved tuning for SVM
# from sklearn.model_selection import GridSearchCV
# parameters_svm = {'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),'clf-svm__alpha': (1e-2, 1e-3)}
# gs_clf_svm = GridSearchCV(text_clf_svm, parameters_svm, n_jobs=-1)
# gs_clf_svm = gs_clf_svm.fit(twenty_train.data, twenty_train.target)
# print(gs_clf_svm.best_score_)
# print(gs_clf_svm.best_params_)
