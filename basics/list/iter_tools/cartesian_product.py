import itertools

num_data = [1, 2, 3]
alpha_data = ['a', 'b', 'c']
result = itertools.product(num_data, alpha_data)
for each in result:
    print(each)

stopwords = ["one", "two", "three"]
data = "The nos in number system starts from one and goes on".split()

# without cartesian product
nos = [4,6,3,9]
for i in nos:
    for j in nos:
        print(i, j)