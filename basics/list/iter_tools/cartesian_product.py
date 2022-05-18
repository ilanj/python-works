import itertools

num_data = [1, 2, 3]
alpha_data = ['a', 'b', 'c']
result = itertools.product(num_data, alpha_data)
for each in result:
    print(each)

stopwords = ["one", "two", "three"]
data = "The nos in number system starts from one and goes on".split()

<<<<<<< HEAD
# without cartesian product
nos = [4,6,3,9]
for i in nos:
    for j in nos:
        print(i, j)
=======
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
