import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task2 = asyncio.create_task(say_after(10, "task2 is done 10 seconds"))
    task1 = asyncio.create_task(say_after(5, "task1 is done 5 seconds"))
    task3 = asyncio.create_task(say_after(3, "task3 is done 3 seconds"))
    task4 = asyncio.create_task(say_after(10, "task4 is done 10 seconds"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task3
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
