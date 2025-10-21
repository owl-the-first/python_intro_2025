from itertools import *

print(*starmap(str.__add__, (product("abcdefgh", "12345678"))))

