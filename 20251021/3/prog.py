from itertools import product


print(', '.join(sorted(filter(lambda s: s.count('TOR') == 2, (''.join(p) for p in product('TOR', repeat=int(input())))))))


import sys
exec(sys.stdin.read())
