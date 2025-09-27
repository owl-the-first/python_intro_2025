s = list(eval(input()))
N = len(s)
a = [s]
for i in range(N - 1):
    a.append(list(eval(input())))
b = [list(eval(input())) for i in range(N)]
result = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(sum(a[i][k] * b[k][j] for k in range(N)))
    result.append(s)
for i in result:
    print(*i, sep=',')
