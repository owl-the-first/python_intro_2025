class A:
    def fun(*args):
        print(f'1: {args}')
    @classmethod
    def cfun(*args):
        print(f'2: {args}')
    @staticmethod
    def sfun(*args):
        print(f'3: {args}')

class B(A):
    pass

print(A.fun)
print(A.cfun)
print(A.sfun)

print(A.fun(1, 2, 3))
print(A.cfun(1, 2, 3))
print(A.sfun(1, 2, 3))

print("-----")

a = A()
a.fun
a.fun(1, 2, 3)

print("-----")

B.cfun(1, 2, 3)

b = B()
b.cfun(1, 2, 3)
