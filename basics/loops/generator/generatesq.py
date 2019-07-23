def returnsq(*nos_list):
    for each in nos_list:
        yield each*each#return returns just a no


sq=returnsq(1,2,3,4)
print(list(sq))
