complex=(23,'afaf', 52.26, True)
print(complex)

for a in complex:
    print(a)
print(complex[1])

if "apple" in complex:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print('apple not found')


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#thistuple[0]=5 no append , remove , pop operations available
x = thistuple.count(5)
no=thistuple.index(5)
print('index of 5=',no)
print('count for 5=',x)
rev=tuple(reversed(thistuple))
print(rev)
sortes_tuples=tuple(sorted(thistuple))
print(tuple(sortes_tuples))

if "apple" in complex:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print('apple not found')


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
#thistuple[0]=5 no append , remove , pop operations available
x = thistuple.count(5)
no=thistuple.index(5)
print('index of 5=',no)
print('count for 5=',x)
rev=tuple(reversed(thistuple))
print(rev)
sortes_tuples=tuple(sorted(thistuple))
print(tuple(sortes_tuples))
