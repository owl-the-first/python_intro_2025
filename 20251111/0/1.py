def multicall(n):
    def mcdecor(fun):
        def decor(*args):
            return [fun(*args) for i in range(n)]
        return decor
    return mcdecor

@multicall(5)
def simple(N):
    return N*2-1

print(*simple(4))
