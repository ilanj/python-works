try:
    from functools import wraps
    from time import sleep
    import threading
    from queue import Queue
    import redis
    import sys
    import time
    import asyncio
    from queue import Queue

    print("{}".format(sys.version))
except Exception as e:
    print("Failed : {} ".format(e))

global r
r = redis.Redis(host="localhost", port=6379, db=0)

queue = Queue()


def cache_async(f):
    async def wrapper(*args, **kwargs):
        num = args[0]
        val = r.get(str(num))
        if val:
            print("cached Value")
            queue.put(int(val))
            return val
        else:
            _ = await f(*args, **kwargs)
            r.set(str(num), str(_))
            queue.put(_)
            return _

    return wrapper


@cache_async
async def computeSquare(num):
    num = num * num
    await asyncio.sleep(3)
    return num


if __name__ == "__main__":
    asyncio.run(computeSquare(4343))
    while True:
        flag = queue.empty()
        if flag:
            pass
        else:
            tem = queue.get()
            break
    print("VALUE : {}".format(tem))

    # val = compute(445)
    # print(val)
