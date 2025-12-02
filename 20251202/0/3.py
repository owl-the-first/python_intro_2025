def itersum(num, n):
    sum = []
    for i in range(n):
        y = yield f"{num} want int | {i}/{n}"
        sum.append(y)
    return sum

def task(num):
    n = yield f"{num} need n"
    res = yield from itersum(num, n)
    yield f"{n = }, {res = }, {sum(res) = }"

def loop(tasks, n):
    for task in tasks:
        print(next(task))

    for i in range(n-1, 1, -1):
        try:
            task = tasks[i % 7 % 3]
            tasks.remove(task)
            print(task.send(i))
            tasks.append(task)
        except StopIteration as E:
            print("One of them is Done")


from collections import deque

tasks = deque(task(i) for i in range(3))

loop(tasks, 30)