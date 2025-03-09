import asyncio


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world ")


# main() directly calling main wont run main
asyncio.run(main())
