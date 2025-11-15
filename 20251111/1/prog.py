def objcount(cls):
    init = cls.__dict__.get('__init__', None)
    delit = cls.__dict__.get('__del__', None)
    cls.counter = 0

    def __init__(self, *args, **kwargs):
        cls.counter += 1
        if init:
            init(self, *args, **kwargs)
        elif hasattr(super(cls, self), '__init__'):
            super(cls, self).__init__(*args, **kwargs)

    def __del__(self):
        cls.counter -= 1
        if delit:
            delit(self)

    cls.__init__ = __init__
    cls.__del__ = __del__
    return cls


import sys
exec(sys.stdin.read())
