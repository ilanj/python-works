def yield_ex():
    yield "one"
    yield "two"
    yield "three"

for each in yield_ex():
    print(each)