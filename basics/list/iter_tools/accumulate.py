'''
The accumulate() function takes a function as an argument. It also takes an iterable.
It returns the accumulated results. The results are themselves contained in an iterable.
'''
import operator
import itertools

def seperator(fun_name):
    print(f"------------{fun_name}------------")
data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
print(seperator("product"))
for each in result:
    print("using mul",each)

print(seperator("max"))
max_no = itertools.accumulate(data, max)
for each in result:
    print("using max",max_no)

#If no function is designated the items will be summed.
print(seperator("sum"))
result = itertools.accumulate(data)
for each in result:
    print("using sum",each)

print(seperator("concat"))
words = ["one", "two", "three"]
result = itertools.accumulate(words, operator.concat)
for each in result:
    print("using mul",each)