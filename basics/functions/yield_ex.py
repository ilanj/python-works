def cube(n):
    for each in range(n):
        yield each*each

for next in cube(15):
    print(next)