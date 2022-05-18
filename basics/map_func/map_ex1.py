# without map---------------

def square(n):
    return n**2

nos = [2, 4, 5, 6, 8, 9]

res = list()
for n in nos:
    res.append(square(n))

print(res)

# with map---------------

<<<<<<< HEAD
res_with_map = list(map(square, nos))
print(res)


# with lambda and map
=======
res = list(map(square, nos))
print(res)


# with lambda and ,ap
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2

sqr = lambda x: x**2
res = list(map(square, nos))
print(res)

<<<<<<< HEAD
nos = ["ddfksju"]
print(str(nos))
=======
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2


