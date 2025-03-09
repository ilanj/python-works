# Decorators
from functools import wraps
import time


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments ({}, {})".format(name, age))


if __name__ == "__main__":
    display_info("Tom", 22)
