s = 0
while (a := eval(input())) > 0:
    s += a
    if s > 21:
        print(s)
        break
else:
    print(a)
