class Vowel:
    __slots__ = ['a', 'e', 'i', 'o', 'u', 'y', '_full']

    def __init__(self, **kwargs):
        for vowel in ['a', 'e', 'i', 'o', 'u', 'y']:
            object.__setattr__(self, vowel, None)
        for key, value in kwargs.items():
            if key in self.__slots__ and key != '_full':
                object.__setattr__(self, key, value)
        object.__setattr__(self, '_full', False)
        self._update_full()

    def _update_full(self):
        all_filled = all(
            object.__getattribute__(self, vowel) is not None
            for vowel in ['a', 'e', 'i', 'o', 'u', 'y']
        )
        object.__setattr__(self, '_full', all_filled)

    @property
    def answer(self):
        return 42

    @answer.setter
    def answer(self, value):
        raise AttributeError("Can't set attribute 'answer'")

    @property
    def full(self):
        return object.__getattribute__(self, '_full')

    @full.setter
    def full(self, value):
        pass

    def __setattr__(self, name, value):
        if name in self.__slots__:
            object.__setattr__(self, name, value)
            self._update_full()
        else:
            raise AttributeError(f"'Vowel' object has no attribute '{name}'")

    def __getattribute__(self, name):
        if name in ['a', 'e', 'i', 'o', 'u', 'y']:
            value = object.__getattribute__(self, name)
            if value:
                raise AttributeError(f"Attribute '{name}' is not set")
            return value
        return object.__getattribute__(self, name)

    def __str__(self):
        result = []
        for vowel in sorted(['a', 'e', 'i', 'o', 'u', 'y']):
            value = object.__getattribute__(self, vowel)
            if value is not None:
                result.append(f"{vowel}: {value}")
        return ", ".join(result)


import sys
exec(sys.stdin.read())


