from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset="train", shuffle=True)

print("categories=", twenty_train.target_names)  # prints all the categoris)
c = -1
for i in twenty_train.target_names:
    c = c + 1
    print(c, i)
