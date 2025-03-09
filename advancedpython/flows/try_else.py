# instead of having many operations in try itself, we can have few in else,
# but any excpetion in else wont be catched.
try:
    with open("for_else.py") as fptr:
        text = fptr.read()

except Exception as e:
    print(e)
else:
    print(text)
