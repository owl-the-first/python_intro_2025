def genf(n):
    for i in range(n):
        yield i*2+1
e = genf(5)
print(e)
# print(next(e))
# print(next(e))
# print(next(e))
# print(next(e))
print("-------")
print(*e)