def msg_decorator(fun):
    # Inner function
    def msg_wrapper(msg):
        print("A decorated line:", fun(msg))

    return msg_wrapper


# Using the decorator
@msg_decorator
def print_name(name):
    print("inisde print_name", name)
    return name


print_name("ila")