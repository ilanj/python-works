import itertools

colors = ['red', 'orange', 'yellow', 'green', 'blue',]
few_colors = itertools.islice(colors, 3)
for each in few_colors:
    print(each)