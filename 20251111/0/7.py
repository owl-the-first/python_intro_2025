class Dsc:
    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return obj._value
    
    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        obj._value = val

    def __delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj._value = None

class A:
    a = Dsc()
    x = 100500

    def __init__(self, name):
        self.a = name

    def __str__(self):
        return f'<{self.a}>'

class Counter:
    cnt = 0

    def __get__(self, obj, cls):
        return self.__class__.cnt
    
    def __set__(self, obj, value):
        self.__class__.cnt = value
