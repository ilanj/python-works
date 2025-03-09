def parent(num):
    def first_child():
        return "Hi, I am first"

    def second_child():
        return "Call me second"

    if num == 1:
        return first_child()
    else:
        return second_child


print(parent(1))
