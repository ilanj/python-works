import time
import timeit


def sample():
    time.sleep(1)
    return "holded for 2 sec"


print(
    timeit.repeat("sample()", setup="from timeit_ex import sample", number=1, repeat=3)
)
