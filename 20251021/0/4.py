def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield x, y
        x += dx
        y += dy

turtle = walk2d()

print(turtle.send(None))
print(turtle.send((1, 1)))
print(turtle.send((1, -1)))