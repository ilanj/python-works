import itertools

for i in itertools.repeat("spam", 7):
    print(i)

# infinite loop
for i in itertools.repeat("spam"):
    print(i)
