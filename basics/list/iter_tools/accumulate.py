'''
The accumulate() function takes a function as an argument. It also takes an iterable.
It returns the accumulated results. The results are themselves contained in an iterable.
'''
import operator
import itertools

data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print("using mul",each)

result = itertools.accumulate(data, max)
for each in result:
    print("using max",each)

#If no function is designated the items will be summed.
result = itertools.accumulate(data)
for each in result:
    print("using sum",each)
