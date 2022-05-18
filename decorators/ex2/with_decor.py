# with parameter

def divcheck(proper_diviion):
    def check(x , y):
        if x==0 or y==0:
            return "zero in input"
        return proper_diviion(x , y)
    return check


@divcheck
def div(a , b):
    return a/b

print(div(5 , 0))
print(div(5 , 6))