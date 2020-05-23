import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task2 = asyncio.create_task(say_after(2, 'world'))
    task1 = asyncio.create_task(say_after(3, "hello"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    # await task1
    await task1

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

