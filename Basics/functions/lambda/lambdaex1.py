def iterate_add(n):
    return lambda x:x+n
fun=iterate_add(50)
print(fun(10))
