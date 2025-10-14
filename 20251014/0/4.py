s = {}

for i in input().split():
    s[i] = s.setdefault(i, 0) + 1

print(s)