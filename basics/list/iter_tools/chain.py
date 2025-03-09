import itertools

colors = ["red", "orange", "yellow", "green", "blue"]
shapes = ["circle", "triangle", "square", "pentagon"]
result = itertools.chain(colors, shapes)
for each in result:
    print(each)
