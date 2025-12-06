import asyncio

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())
    i, j = start, middle
    k = start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()


async def _copy_run(A1, A2, start, finish, event_in, event_out):
    await event_in.wait()
    A2[start:finish] = A1[start:finish]
    event_out.set()


async def mtasks(A):
    n = len(A)
    A0 = list(A)
    B0 = [None] * n
    tasks = []
    if n == 0:
        return tasks, []
    width = 1
    src, dst = A0, B0
    events_src = {}
    for s in range(0, n, width):
        e = asyncio.Event()
        e.set()
        events_src[s] = e
    while width < n:
        events_dst = {}
        for start in range(0, n, 2 * width):
            middle = min(start + width, n)
            finish = min(start + 2 * width, n)
            out_event = asyncio.Event()
            events_dst[start] = out_event
            if middle < finish:
                tasks.append(
                    merge(src, dst, start, middle, finish,
                        events_src[start], events_src[middle], out_event)
                )
            else:
                tasks.append(
                    _copy_run(src, dst, start, finish,
                            events_src[start], out_event)
                )
        src, dst = dst, src
        events_src = events_dst
        width *= 2
    return tasks, src


import sys
exec(sys.stdin.read())
