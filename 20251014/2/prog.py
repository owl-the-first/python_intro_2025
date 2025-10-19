from math import *

func_names = {}
func_names['quit'] = None
k = 0
lines = []
while True:
    s = input()
    lines.append(s)
    if s.startswith("quit "):
        break
for s in lines:
    if s[0] == ":":
        a = s[1:].split()
        func_names[a[0]] = (a[1:-1], a[-1])
        k += 1
        continue
    if s.startswith("quit "):
        k += 1
        f = s.split(maxsplit=1)[1].strip()
        f = f[1:-1] if f[0] in "\"'" and f[-1] == f[0] else f
        print(f.format(len(func_names), k))
        break
    a = s.split(maxsplit=1)
    params, expr = func_names[a[0]]
    if len(a) == 1:
        p = []
    else:
        p = [a[1]] if len(params) == 1 else a[1].split()
    converted = []
    for i in p:
        i = i.strip()
        converted.append(i[1:-1]) if i[0] in "\"'" and i[-1] == i[0] else converted.append(eval(i, globals()))
    print(eval(expr, globals(), dict(zip(params, converted))))
    k += 1
