from collections import UserString


class DivStr(UserString):
    def __init__(self, seq=''):
        super().__init__(seq)

    def __floordiv__(self, n):
        if n <= 0:
            return iter([])
        size = len(self) // n
        for i in range(n):
            yield DivStr(self.data[i * size:(i + 1) * size])

    def __mod__(self, n):
        if n <= 0:
            return DivStr(self.data)
        size = len(self) // n
        return DivStr(self.data[n * size:])


import sys
exec(sys.stdin.read())
