# demo of while if
# when break is used, else wont be executed
def while_else():
    itr = 0
    while itr < 10:
        print(itr)
        itr = itr + 1
    else:
        print("after breaking")
        print(itr)


# if break used
def while_else_break():
    itr = 0
    while itr < 10:
        print(itr)
        itr = itr + 1
        if itr == 5:
            break
    else:
        print("after breaking")
        print(itr)


while_else_break()
