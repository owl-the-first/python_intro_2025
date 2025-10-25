from itertools import islice


def slide(seq, n):
    it = iter(seq)
    window = list(islice(it, n))
    while window:
        yield from window
        window.pop(0)
        next_elem = list(islice(it, 1))
        if next_elem:
            window.append(next_elem[0])


import sys
exec(sys.stdin.read())
