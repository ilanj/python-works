import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task2 = asyncio.create_task(say_after(10, "world"))
    task1 = asyncio.create_task(say_after(5, "hello"))
    task3 = asyncio.create_task(say_after(3, "i am done parallely"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
