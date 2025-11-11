def istype(typ):
    def istyp(fun):
        def decor(*args):
            if any(not isinstance(arg, typ) for arg in args):
                raise TypeError(f"All args must be {typ}")
            return fun(*args)
        return decor
    return istyp
