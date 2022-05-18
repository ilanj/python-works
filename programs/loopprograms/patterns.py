n = int(input("enter a integer no"))

def rt_angle():
    for i in range(n):
        for j in range(i):
            print("*  ", end = "")
        print()

def triangle():
    spaces = 0
    for i in range(n):
        spaces = n - i
        for k in range(spaces):
            print(" ", end="")
        for j in range(i):
            print("* ", end = "")
        print()


def rt_opp_traingle():
    spaces = 0
    for i in range(n):
        spaces = n - i
        for k in range(spaces):
            print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()

if __name__ =="__main__":
    rt_angle()
    rt_opp_traingle()
    triangle()
