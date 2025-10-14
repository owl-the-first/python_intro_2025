from string import ascii_lowercase
from timeit import Timer

wov = set("aouie")
con = set(ascii_lowercase) - wov

def fun(s):
    return (len(s & wov), len(s & con))

s = set(input())
T = Timer("fun(s)", globals=globals())

res = T.autorange()
print(res)
