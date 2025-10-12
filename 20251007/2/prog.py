from math import *


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


def dda(x0, y0, x1, y1, a, H):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(1, int(round(abs(dy))))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x0, y0
    for i in range(steps + 1):
        ix = round(x)
        iy = round(y)
        if 0 <= iy < H:
            a[H - 1 - iy][ix] = '*'
        x += x_inc
        y += y_inc


data = input().split()
W, H, A, B = map(int, data[:4])
expr = " ".join(data[4:])
xs, ys, xs_scaled, ys_scaled = [], [], [], []
for i in range(W):
    xs.append(scale(0, W - 1, A, B, i))
for x in xs:
    ys.append(eval(expr, {"x": x, **globals()}))
y_min, y_max = min(ys), max(ys)
if y_min == y_max:
    y_min -= 1
    y_max += 1
ys_scaled = []
for y in ys:
    ys_scaled.append(scale(y_min, y_max, 0, H - 1, y))
a = []
for i in range(H):
    a.append([])
    for j in range(W):
        a[i].append(" ")
for i in range(W - 1):
    x0, y0 = i, ys_scaled[i]
    x1, y1 = i + 1, ys_scaled[i + 1]
    dda(x0, y0, x1, y1, a, H)
for i in a:
    print("".join(i))
