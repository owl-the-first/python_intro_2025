def sub(a, b):
    t = type(a)
    if t == int or t == float or t == complex:
        return a - b
    else:
        result = []
        for i in a:
            if i not in b:
                result.append(i)
        return t(result)

a = eval(input())
b = a[1]
a = a[0]
print(sub(a, b))