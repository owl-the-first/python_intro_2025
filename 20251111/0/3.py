class ParDec:
    def __init__(self, par):
        class Dec:
            def __init__(self, fun):
                pass
            def __call__(self, *args):
                print(*args)
        return Dec
    
@ParDec(8)
def fun(a, b):
    return a+b
