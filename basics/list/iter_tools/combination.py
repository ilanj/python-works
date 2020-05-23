import itertools

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)

print("-------------------------------------")

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations_with_replacement(shapes, 2)
for each in result:
    print(each)