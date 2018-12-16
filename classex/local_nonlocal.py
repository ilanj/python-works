def custom_print():
    def local_print():
        name="i am local"
        print("inside local ",name)

    def nonlocal_print():
        nonlocal  name #this nonlocal will work only if it has binding(local var outside this function) and cant be initialized at same line
        name="i am nonlocal"
        print("inside non local ",name)

    def global_print():
        global name
        name="i am global"
        print("inside global ",name)
    name="i am local name"
    local_print()
    nonlocal_print()
    global_print()
    print(name)

name="i am local"
print(name)
custom_print()
print(name)