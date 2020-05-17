import asyncio

async def nested():
    return 42

async def main1():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    print(nested())
    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

async def main2():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)

asyncio.run(main1())
asyncio.run(main2())