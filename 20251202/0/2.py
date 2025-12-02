async def meet(n):
    for i in range(n):
        yield f"{i}: Hello"
    return f"You {n}: Bye!"

async def meeting(m):
    for i in range(m):
        res = await meet(3)
        print(f"<{i}>: {res}")
    return "FIN"



i = meeting(2)
try:
    counter = 0
    while True:
        print('>>>', counter)
        i.send(None)
except StopIteration as E:
    print(E.value)