def MINF(*funs):
    def fun(x):
        return min([f(x) for f in funs])
    return fun
