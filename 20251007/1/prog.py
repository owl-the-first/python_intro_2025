from fractions import Fraction


def check_solution(values):
    a = []
    for i in values:
        a.append(Fraction(str(i)))
    s, w = a[0], a[1]
    power_A = int(a[2])
    coef_A = a[3:4 + power_A]
    power_B = int(a[4 + power_A])
    coef_B = a[5 + power_A: 6 + power_A + power_B]
    A, B, = 0, 0
    if coef_A:
        for c in reversed(coef_A):
            A = A * s + c
    if coef_B:
        for c in reversed(coef_B):
            B = B * s + c
    if B == 0:
        return False
    return A / B == w


print(check_solution(eval(input())))