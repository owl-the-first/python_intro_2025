class Num:
    def __init__(self):
        self.data = {}

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return self.data.get(id(obj), 0)

    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            val = value.real
        elif hasattr(value, '__len__'):
            val = len(value)
        else:
            val = value
        self.data[id(obj)] = val


import sys
exec(sys.stdin.read())
