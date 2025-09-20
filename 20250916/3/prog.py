N = eval(input())
i = 0
while i < 3:
    j = 0
    while j < 3:
        a = (N + i) * (N + j)
        b = a
        s = 0
        while b > 0:
            s += b % 10
            b //= 10
        if j == 2:
            if s == 6:
                print(N + i, "*", N + j, "=", ':=)')
            else:
                print(N + i, "*", N + j, "=", a)
        else:
            if s == 6:
                print(N + i, "*", N + j, "=", ':=)', end=' ')
            else:
                print(N + i, "*", N + j, "=", a, end=' ')
        j += 1
    i += 1
