import asyncio
import time


async def factorial(name, number):
    f = 1.0
    await asyncio.sleep(1)
    print(f"Task {name}: Compute factorial({number})...")
    for i in range(2, number + 1):
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    # Schedule three calls *concurrently*:
    print(f"parallel started at {time.strftime('%X')}")
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(f"completed at {time.strftime('%X')}")


asyncio.run(main())  # parallel
print(
    "----------------------------------------------------------------------------------------------------------"
)


def factorial_seq(name, number):
    f = 1.0
    time.sleep(1)
    print(f"Task {name}: Compute factorial({number})...")
    for i in range(2, number + 1):
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


def seq():
    # Schedule three calls *concurrently*:
    print(f"Sequential started at {time.strftime('%X')}")
    factorial_seq("A", 2),
    factorial_seq("B", 3),
    factorial_seq("C", 4),
    print(f"ended at {time.strftime('%X')}")


# seq()
