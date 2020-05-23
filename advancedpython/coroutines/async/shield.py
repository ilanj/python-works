'''
If it is desired to completely ignore cancellation (not recommended) the shield() function
should be combined with a try/except clause, as follows:
19 May 2020 @: ilanchezhiancse@gmail.com
'''
import asyncio
from asyncio import shield, CancelledError


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    try:
        res = await shield(factorial("a", 4))
    except CancelledError:
        res = None

asyncio.run(main())
