def istype(typ):
    class IsTyp:
        def __init__(self, fun):
            self.dun = fun

        def __call__(self, *args):
            if any(not isinstance(arg, typ) for arg in args):
                raise TypeError(f"All args must be {typ}")
            return self.fun(*args)
    return IsTyp



# @istype(str)
# def fun(a, b):
#     return a+b
# print(fun(a, b))
