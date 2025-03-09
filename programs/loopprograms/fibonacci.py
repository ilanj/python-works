a, b = -1, 1

count = 15
while a < 15:
    # temp = a
    # a = b
    # b = temp + b
    a, b = b, a + b
    print(b)
