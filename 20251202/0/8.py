import asyncio

async def a(event):
    print("NOT URA")
    await event.wait()
    print("USA")

async def main():
    e = asyncio.Event()
    task = asyncio.create_task(a(e))
    await asyncio.sleep(1)
    e.set()
    await task



asyncio.run(main())