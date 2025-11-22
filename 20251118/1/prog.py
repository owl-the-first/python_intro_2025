import sys


data = sys.stdin.buffer.read()
N = data[0]
tail = data[1:]
L = len(tail)
if N == 0:
    sys.stdout.buffer.write(bytes([0]))
else:
    a = []
    for i in range(N):
        a.append(tail[i * L // N:(i + 1) * L // N])
    a.sort()
    sys.stdout.buffer.write(bytes([N]) + b''.join(a))
