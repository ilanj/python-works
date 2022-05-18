import itertools
import operator

data = [(2, 6), (8, 4), (7, 3)]
result = itertools.starmap(operator.mul, data)
for each in result:
    print(each)