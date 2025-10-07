import decimal
import math


def esum(N, one):
    e = 0
    for i in range(1, N):
        e += one(str(1 / math.factorial(i)))
    return e


for t in float, decimal.Decimal:
    print(esum(100, t))
