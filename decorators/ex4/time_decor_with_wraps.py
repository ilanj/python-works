'''
<<<<<<< HEAD
It updates the wrapper function to look like wrapped function by copying attributes such as __name__,
__doc__ (the docstring), etc.if u remove wraps, called function details will be used
=======
It updates the wrapper function to look like wrapped function by copying attributes such as __name__, __doc__ (the docstring), etc.
if u remove wraps, called function details will be used
>>>>>>> 7aea316fb7211c19240808b49e999c9f2e0561f2
'''
import threading
import time
from functools import wraps


def time_capture(time_log_fun):
    @wraps(time_log_fun)
    def fun_logger(*args):
        """ to calculate time """
        t1 = time.time()
        result = time_log_fun(*args)
        t2 = time.time() - t1
        print(f"{time_log_fun.__name__} completed in {t2} secs")
        return result
    return fun_logger

@time_capture
def sum_of_nos(*args):
    """ to calculate sume of nos"""
    time.sleep(1)
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum

print(sum_of_nos(1, 2, 3, 4, 5))
print(sum_of_nos.__name__)
print(sum_of_nos.__doc__)