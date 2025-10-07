from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

W, H = eval(input())
A, B = eval(input())

screen = [[' '] * W for i in range(H)]
for i in range(W):
    x = scale(0, W - 1, A , B,  i)
    y = sin(x)
    k = round(scale(-1, 1, 0, H - 1, y))
    screen[H - k - 1][i] = '*'
print("\n".join("".join(i) for i in screen))
