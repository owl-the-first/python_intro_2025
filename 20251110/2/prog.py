import sys


class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(s):
    try:
        coords = eval(s)
        if not (isinstance(coords, tuple) and len(coords) == 3):
            raise InvalidInput()
        point1, point2, point3 = coords
        for point in (point1, point2, point3):
            if not (isinstance(point, tuple) or isinstance(point, list)):
                raise InvalidInput()
            if len(point) != 2:
                raise InvalidInput()
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = point3
        x1, y1 = float(x1), float(y1)
        x2, y2 = float(x2), float(y2)
        x3, y3 = float(x3), float(y3)
    except:
        raise InvalidInput()
    if not all(isinstance(i, (int, float)) for i in [x1, y1, x2, y2, x3, y3]):
        raise BadTriangle()
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) // 2
    if area == 0:
        raise BadTriangle()
    return round(area, 2)


for i in sys.stdin:
    i = i.strip()
    if not i:
        continue
    try:
        area = triangleSquare(i)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{area:.2f}")
