from functools import reduce

nos=range(1,11)
sum=reduce(lambda x,y:x+y, nos)
print(sum)