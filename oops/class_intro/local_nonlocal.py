"""
1.this nonlocal will work only if it has binding(local var outside this function) and cant be initialized at same line
non local variables are for nested methods
"""


def custom_print():
    name = "i am class variable binding for non local variable"

    def local_print():
        name = "i am local"
        print("inside local ", name)

    def nonlocal_print():
        nonlocal name
        name = "i am nonlocal"
        print("inside non local ", name)

    def global_print():
        global name
        name = "i am global"
        print("inside global ", name)

    print("name inside custom print function -------------", name)
    local_print()
    nonlocal_print()
    print("name inside custom print function -------------", name)
    global_print()


# name="i am outside class"
# print(name)
custom_print()
print(name)
