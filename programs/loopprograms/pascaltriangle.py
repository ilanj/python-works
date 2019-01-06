n=6
for r in range(n):
    for space in range(n - r):
        print(' ', end="")
    for c in range(r):
        print('* ',end="")
    print()