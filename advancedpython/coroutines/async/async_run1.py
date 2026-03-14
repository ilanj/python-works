import asyncio


async def main():
    print("hello")
    await asyncio.sleep(3)
    print("world ")


# main() directly calling main wont run main
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
asyncio.run(main())
