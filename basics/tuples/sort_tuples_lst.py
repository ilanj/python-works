'''
sort list of tuples
'''
import random

tuples_list = list()

for nos in range(10):
    tuples_list.append((random.randint(1,50), (random.randrange(0,100,2), "test")))

print(tuples_list)
print(sorted(tuples_list))
print(reversed(tuples_list))
print(sorted(tuples_list, reverse=True))