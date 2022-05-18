import itertools
mylist = ["one", "two", "three"]
text = "this is a sample  text one"

print([True for each in mylist if each in text])