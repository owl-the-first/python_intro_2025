from math import *

def Calc(s, t, u):
    def f(x):
        s_val = eval(s, globals(), {'x': x})
        t_val = eval(t, globals(), {'x': x})
        return eval(u, globals(), {'x': s_val, 'y': t_val})
    return f

F = Calc(*eval(input()))
print(F(eval(input())))
