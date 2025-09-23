a = [d for d in range(11, 28) if d % 2 == 1 and '3' not in str(d)]
print(a)

b = any([0, 0, "", [], 234, 0.0])
print(b)
