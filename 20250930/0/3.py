def binN(n, ones, base=0):
    if n == 0:
        if ones == 0:
            print(base)
    else:
        if ones:
            binN(n - 1, ones - 1, base * 2 + 1)
        binN(n - 1, ones, base * 2)
