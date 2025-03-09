import asyncio


async def get_sq(n):
    await asyncio.sleep(5)
    return n * n


async def get_cube(n):
    res = n * n * n
    await asyncio.sleep(5)
    return res


async def main():
    print(await asyncio.gather(get_sq(4), get_cube(4)))


asyncio.run(main())
