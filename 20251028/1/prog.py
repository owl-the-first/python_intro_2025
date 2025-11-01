class Omnibus:
    _counters = {}
    _attributes = {}

    def __init__(self):
        self._id = id(self)
        Omnibus._attributes[self._id] = set()

    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
            return
        if name not in Omnibus._attributes[self._id]:
            Omnibus._attributes[self._id].add(name)
            Omnibus._counters[name] = Omnibus._counters.get(name, 0) + 1

    def __getattr__(self, name):
        return Omnibus._counters.get(name, 0)

    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
            return
        if name in Omnibus._attributes[self._id]:
            Omnibus._attributes[self._id].remove(name)
            if Omnibus._counters.get(name, 0) > 0:
                Omnibus._counters[name] -= 1
                if Omnibus._counters[name] == 0:
                    del Omnibus._counters[name]

    def __del__(self):
        if self._id in Omnibus._attributes:
            attrs = Omnibus._attributes[self._id].copy()
            for attr in attrs:
                if Omnibus._counters.get(attr, 0) > 0:
                    Omnibus._counters[attr] -= 1
                    if Omnibus._counters[attr] == 0:
                        del Omnibus._counters[attr]
            del Omnibus._attributes[self._id]

import sys
exec(sys.stdin.read())
