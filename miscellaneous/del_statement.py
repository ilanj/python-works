class Test:
    def __init__(self):
        print()


x = Test
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# del is also used in listes
nos = [1, 2, 3, 4]
del nos[0]
print(nos)
