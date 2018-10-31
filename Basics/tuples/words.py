complex=(23,'afaf', 52.26, True)
for a in complex:
    print(a)
print(complex[1])

if "apple" in complex:
  print("Yes, 'apple' is in the fruits tuple")
else:
    print('apple not found')


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
no=thistuple.index(5)
print('index of 5=',no)
print('count for 5=',x)
