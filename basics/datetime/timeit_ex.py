import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time: {elapsed_time:.6f} seconds")
        return result
    return wrapper


print(
    timeit.repeat("sample()", setup="from timeit_ex import sample", number=1, repeat=3)
)
@timeit
def pritning_arg():
    print("hello")

print(pritning_arg())
