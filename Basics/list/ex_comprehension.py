#syntax:[expression followed by a for (more for is optiona;) (if is optional)]
nos=range(1,11)

sq=[(x**2) for x in nos if x%2==0 ]
print(sq)

# even=[(x) for x in nos if x%2==0]
#
# print(even)
#
# odd=[]
# for x in nos:
#     if x%2==1:
#         odd.append(x)
# print(odd)