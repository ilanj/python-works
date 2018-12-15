#whether a number is possitive
import random
import numpy
#n=random.randint(1000,9999)
n=11

if n %3 ==0:
    if n % 5==0:
        print(n, " is divisible by both 3 and 5")
    else:
        print(n, ' is only divisibly by 3')
else:
    if n % 5 is 0:
        print(n, 'is divisibly by 5 only')
    else:
        print(n, 'is not divisible by both 3 and 5')

print("exiting if")

