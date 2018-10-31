import random

ex=[]
#n=eval(input("enter n"))
n=random.randint(5,8)
for i in range(0,n):
    ex.append(random.randint(10,65))
print('original',ex)
ex=list(reversed(ex))
print('reversed',ex)
ex=list(reversed(ex))
print('back to originals',ex)
ex=list(sorted(ex))
print('after sorting',ex)
