"""
coroutine asyncio.wait_for(aw, timeout, *, loop=None)
Wait for the aw awaitable to complete with a timeout.
19 May 2020 @ ilanchezhiancse@gmail.com
"""

import asyncio


async def print_res():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print("yay!")


async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(print_res(), timeout=1.0)
    except asyncio.TimeoutError as e:
        print("timeout!")


asyncio.run(main())
