def is_called():
    def is_returned():
        print("Hello")
        return "return hello"

    return is_returned


new = is_called()

# Outputs "Hello"
print(new())
print(new.__name__)
