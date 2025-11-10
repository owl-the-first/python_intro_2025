def itemget(collection, idx):
    return collection[idx]

def safeindex(function, *args):
    try:
        return function(*args)
    except IndexError:
        return None

list(safeindex(itemget, "qwe", "qwe"))