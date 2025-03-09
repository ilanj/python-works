"""
sum using lambda
"""

sum = lambda x, y, z: x + y + z

print(sum(5, 6, 8))

"""
split using lambda 
"""
extension = lambda fname: fname.split(".")[-1]
print(extension("un_named.jpeg"))
