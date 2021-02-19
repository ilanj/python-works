def decorator_function(original_fun):
    def wrapper_function():
        return original_fun
    return wrapper_function()

@decorator_function
def display():
    print('display function ')

decorated_display = decorator_function(display())
decorated_display