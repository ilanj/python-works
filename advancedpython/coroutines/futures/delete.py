import asyncio


async def target(loop, timeout=None):
    future = asyncio.run_coroutine_threadsafe(add(1, b=2), loop)
    return future.result()


async def add(a, b):
    # await asyncio.sleep(1)
    return a + b


async def main():
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, target, loop)
    assert loop.run_until_complete(future) == 3


asyncio.run(main())
