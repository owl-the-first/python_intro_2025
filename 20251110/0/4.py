class A:
    def __init__(self, val):
        self.val = val

class B(A):
    def __init__(self, val):
        print("Do it, A")
        super().__init__(val)
        print(f"<{self.val}>")

a = A(123)
b = B(456)
