"""
sort list of tuples
"""

import random

tuples_list = list()

tuples_list.append((1, 12))
tuples_list.append((5, 6))
tuples_list.append((3, 4))
print(tuples_list)
print(sorted(tuples_list))
print(sorted(tuples_list, reverse=True))
