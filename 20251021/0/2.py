def genf(n):
    for i in range(1, n):
        yield sum(1/(j**2) for j in range(1, i+1))

e = genf(7)
print(*e)