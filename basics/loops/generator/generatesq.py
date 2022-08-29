def get_squares(*args):
    for arg in args:
        yield arg * arg

print(list(get_squares(2,4,6,8)))
def returnsq(*nos_list):
    for each in nos_list:
        yield each*each#return returns just a no


sq=returnsq(1,2,3,4)
print(list(sq))

for each in returnsq(1, 2, 3):
    print(each)
