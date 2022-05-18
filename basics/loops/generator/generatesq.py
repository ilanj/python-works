def get_squares(*args):
    for arg in args:
        yield arg * arg

print(list(get_squares(2,4,6,8)))