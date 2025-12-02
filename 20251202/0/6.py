import asyncio

async def task(num, n, delay):
    for i in range(n):
        print(num, i)
        await asyncio.sleep(delay)
    return f"task{num}"

async def main():
    # t1 = asyncio.create_task(task(0, 4, 2))
    # t2 = asyncio.create_task(task(1, 6, 1))
    # await t1
    # await t2
    tasks = await asyncio.gather(task(0, 4, 2), task(1, 6, 1))
    print(tasks)

asyncio.run(main())