def print_message(a):
    print("first function")

def print_message(a,b):# latest defined function, so only this will be called
    print("second function")

print_message("fdd","ded")