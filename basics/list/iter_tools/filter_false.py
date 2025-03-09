import itertools

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = itertools.filterfalse(lambda x: x < 5, data)
for each in result:
    print(each)
