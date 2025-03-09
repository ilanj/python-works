"""
sorting asc and desc
"""

nos = [4, 1, 3, 5, 2, 4, 5, 4, 6, 4, 4, 4]
nos.sort()
print(nos)

nos.sort(reverse=True)
print(nos)

"""
frequencies
"""
print(nos.count(4))
print(nos.index(4))  # first occurrence
