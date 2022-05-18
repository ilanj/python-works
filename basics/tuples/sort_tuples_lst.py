'''
sort list of tuples
'''
import random

tuples_list = list()

for nos in range(10):
    tuples_list.append((random.randint(1,50), (random.randrange(0,100,2), "test")))

print(tuples_list)
<<<<<<< HEAD
print(sorted(tuples_list))
print(reversed(tuples_list))
=======
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
print(sorted(tuples_list, reverse=True))