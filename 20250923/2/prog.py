a = list(eval(input()))
for i in range(len(a) - 1):
    f = False
    for j in range(len(a) - i - 1):
        if (a[j] ** 2 % 100) > (a[j + 1] ** 2 % 100):
            a[j], a[j + 1] = a[j + 1], a[j]
            f = True
    if not f:
        break
print(a)
