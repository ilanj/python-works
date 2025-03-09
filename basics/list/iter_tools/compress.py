import itertools

shapes = ["circle", "triangle", "square", "pentagon"]
selections = [True, False, True, False]
result = itertools.compress(shapes, selections)
for each in result:
    print(each)
