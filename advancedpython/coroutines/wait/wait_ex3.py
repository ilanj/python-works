import asyncio
from asyncio import ALL_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION, create_task


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


def create_future():
    pass


async def main():
    call_fact1 = create_task(factorial("a" , 4))
    call_fact2 = create_task(factorial("a" , 1))
    call_fact3 = create_task(factorial("a" , 3))
    call_fact4 = create_task(factorial("a" , 5))
    calls = [call_fact1, call_fact2, call_fact3, call_fact4]
    # done, pending = await asyncio.wait(calls, timeout=None, return_when=FIRST_COMPLETED)
    # done, pending = await asyncio.wait(calls, timeout=None, return_when=ALL_COMPLETED)
    # done, pending = await asyncio.wait(calls, timeout=None, return_when=FIRST_EXCEPTION)

asyncio.run(main())
