import inspect

class dump(type):
    def __new__(mcls, name, bases, namespace):
        new_namespace = {}
        for attr, value in namespace.items():
            if inspect.isfunction(value):
                def make_wrapper(func, fname):
                    def wrapper(*args, **kwargs):
                        if len(args) >= 1:
                            print(f"{fname}: {args[1:]}, {kwargs}")
                        else:
                            print(f"{fname}: {args}, {kwargs}")
                        return func(*args, **kwargs)
                    return wrapper
                new_namespace[attr] = make_wrapper(value, attr)
            else:
                new_namespace[attr] = value
        return super().__new__(mcls, name, bases, new_namespace)


import sys
exec(sys.stdin.read())
