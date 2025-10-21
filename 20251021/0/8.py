import itertools 


a, b, c = itertools.starmap(int, (("123123", 4), ("deadbeef", 16), ("1000", 10)))
print(a, b, c)
print(*itertools.combinations("qwerty", 3))
print()
print(list(itertools.combinations("qwerty", 3)))
print()
print(list(itertools.combinations("qaaa", 3)))
print()
