char_set=set()

n=int(input("enter how many chars u want to enter"))

for i in range(n):
    char_set.add(eval(input("enter a no")))
print(char_set)
print(sum(char_set))
print(frozenset(sorted(char_set)))
<<<<<<< HEAD
print(sorted(char_set))
=======
print(sorted(sorted(char_set)))
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
# print(reversed((char_set)))#will not work


