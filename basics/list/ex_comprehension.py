#syntax:[expression followed by a for (more for is optiona;) (if is optional)]
nos=range(1,11)

sq=[(x**2) for x in nos if x%2==0 ]
print(sq)


nos1=[12,34,5,67,89,76]
print(nos1[1])
# even=[(x) for x in nos if x%2==0]
#
# print(even)
#
# odd=[]
# for x in nos:
#     if x%2==1:
#         odd.append(x)
# print(odd)