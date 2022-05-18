import itertools

colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in itertools.zip_longest(data, colors, fillvalue=None):
    print(each)