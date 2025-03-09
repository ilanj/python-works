import itertools

# infinite loop
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for color in itertools.cycle(colors):
    print(color)
