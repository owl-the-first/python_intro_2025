from itertools import *

def divn(n, seq):
	yield from filterfalse(lambda x: x%n, seq)

print(*list(divn(5, range(33))))
