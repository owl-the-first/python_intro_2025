from itertools import *

def raw():
	s = 0
	for i in count(1):
		s += 1/i**2
		yield s

r = raw()
print(*list(islice(dropwhile(lambda x: x < 1.6, raw()), 10)))
