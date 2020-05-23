import asyncio
import time


async def main1():
    print("started 1")
    await asyncio.sleep(4)
    return 111
async def main2():
    print("started 2")
    await asyncio.sleep(4)
    return 222
async def main3():
    print("started 3")
    await asyncio.sleep(4)
    return 333
async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(main1())
    task2 = loop.create_task(main2())
    task3 = loop.create_task(main3())
    tasks = [task1, task2, task3]
    res= await asyncio.gather(
        task1, task2, task3
    )
    print(res)

if __name__ == '__main__':
    print(time.strftime('%X'))
    asyncio.run(main())
    print(time.strftime('%X'))

    # loop = asyncio.get_event_loop()
    # # task1 = loop.create_task(main1())
    # # task2 = loop.create_task(main2())
    # # task3 = loop.create_task(main3())
    # # tasks = [task1, task2, task3]
    # await asyncio.gather(
    #    main1()
    # )
    # res = []
    # try:
    #     res.append(loop.run_until_complete(main1()))
    #     res.append(loop.run_until_complete(main2()))
    #     res.append(loop.run_until_complete(main3()))
    #     print(res)
    # except:
    #     pass
    # finally:
    #     loop.close()