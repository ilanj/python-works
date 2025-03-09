import time
from functools import wraps

from joblib import Parallel, delayed


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@timeit
def pow_five(n):
    time.sleep(1)


from joblib import Parallel, delayed


def pow_five(n):
    # time.sleep(1)
    if n == 2:
        time.sleep(1)
    print(n**5)


if __name__ == "__main__":
    Parallel(n_jobs=4, backend="multiprocessing")(
        delayed(pow_five)(n) for n in range(4)
    )
