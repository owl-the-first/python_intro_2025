class Rectangle:
    rectnt = 0
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        __class__.rectnt += 1
        setattr(self, f"rect_{self.rectnt}", self.rectnt)
    def __str__(self):
        return f"{__class__.rectnt}{self.x1, self.y1}{self.x1, self.y2}{self.x2, self.y1}{self.x2, self.y2}"
    def square(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1)
    def __lt__(self, other):
        return self.square() <  other.square()
    def __eq__(self, other):
        return self.square() ==  other.square()
    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.x2 * num, self.y1 * num, self.y2 * num)
    __rmul__ = __mul__
    def __getitem__(self, index):
        if index == 0:
            return (self.x1, self.y1)
        elif index == 1:
            return (self.x1, self.y2)
        elif index == 2:
            return (self.x2, self.y2)
        elif index == 3:
            return (self.x2, self.y1)
        else:
            raise IndexError
    def __del__(self):
        self.__class__.rectnt -= 1
        print()


R = Rectangle(1, 1, 2, 2)
print(R)
R = Rectangle(1, 0, 2, 3)
print(R)
