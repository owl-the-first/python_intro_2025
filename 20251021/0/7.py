from itertools import *

def repeater(seq, n):
	for el in seq:
		yield from repeat(el, n)

print(*list(repeater(iter("ABC"), 5))
)
