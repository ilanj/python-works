# without map---------------

def square(n):
    return n**2

nos = [2, 4, 5, 6, 8, 9]

res = list()
for n in nos:
    res.append(square(n))

print(res)

# with map---------------

res_with_map = list(map(square, nos))
print(res)


# with lambda and map

sqr = lambda x: x**2
res = list(map(square, nos))
print(res)

nos = ["ddfksju"]
print(str(nos))


