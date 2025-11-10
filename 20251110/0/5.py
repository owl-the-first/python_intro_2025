class A:
    def __str__(self):
        return __class__.__name__


class B(A):
    def __str__(self):
        return f"{super().__str__()}:{__class__.__name__}"


class C(B):
    def __str__(self):
        return f"{super().__str__()}:{__class__.__name__}"


print(A())
print(B())
print(C())
