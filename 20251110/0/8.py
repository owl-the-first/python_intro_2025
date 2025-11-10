def div(a, b, eps):
    if abs(b) < abs(eps):
        raise ZeroDivisionError("ggjdggjg")
    return a / b

print(div(1, 2, 10))
