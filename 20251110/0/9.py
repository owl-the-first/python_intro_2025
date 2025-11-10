class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

k = 0
classessss = [A, B, C, D]
for i in [A, B, C, D]:
    for j in [A, B, C, D]:
        if C in (i, j):
            try:
                class E(i, j):
                    pass
                print(i, j)
                e = E()
                k += 1
            except:
                continue
print(k)