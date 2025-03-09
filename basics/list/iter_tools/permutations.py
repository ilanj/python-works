import itertools

alpha_data = ["a", "b", "c"]
result = itertools.permutations(alpha_data)
for each in result:
    print(each)
