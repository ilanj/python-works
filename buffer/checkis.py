import itertools

dict_map = {'a' : 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2,
            'f' : 3, 'g': 3, 'h': 3, 'i': 4, 'j': 4,
            'k' : 4, 'l': 5, 'm': 5, 'n': 5, 'o': 6,
            'p' : 6, 'q': 6, 'r': 7, 's': 7, 't': 7,
            'u' : 8, 'v': 8, 'w': 8, 'x': 9, 'y': 9,
            'z' : 9}

inp = input()
is_divisible = 0
length = len(inp)
for each in range(length):
    result = itertools.combinations(inp, each+1)
    for each in result:
        print(dict_map[each])