from functools import wraps
import redis
import time

global r
r = redis.Redis(host="localhost", port=6379, db=0)


def cache(function=None):
    @wraps(function)
    def wrapper(*args, **kwargs):
        num = args[0]

        val = r.get(str(num))

        if val:
            print("cached Value")
            return val
        else:

            _ = function(*args, **kwargs)
            r.set(str(num), str(_))
            return _

    return wrapper


@cache
def compute(num):
    num = num * num
    time.sleep(4)
    return num


if __name__ == "__main__":
    val = compute(5)
    print(val)
