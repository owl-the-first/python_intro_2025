import asyncio

async def snd():
    evsnd.set()
    print("snd: gen evsnd")

async def mid(k):
    await evsnd.wait()
    print(f"mid({k}): rcv evsnd")
    globals()[f"evmid{k}"].set()
    print(f"mid({k}): gen evmid{k}")

async def rcv():
    await evmid0.wait()
    print("rcv: rcv evmid0")
    await evmid1.wait()
    print("rcv: rcv evmid1")



evsnd, evmid0, evmid1 = asyncio.Event(), asyncio.Event(), asyncio.Event()

async def main():
    _ = await asyncio.gather(snd(), mid(1), mid(0), rcv())
    print("GOTOVO")


asyncio.run(main())