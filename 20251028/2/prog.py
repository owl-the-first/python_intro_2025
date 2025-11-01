class Triangle:
    def __init__(self, *points):
        self.vertices = tuple(tuple(p) for p in points)

    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.vertices
        return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2.0

    def __abs__(self):
        area = self.area()
        return 0 if area < 1e-10 else area

    def __bool__(self):
        return abs(self) > 1e-10

    def __lt__(self, other):
        return abs(self) < abs(other)

    def _point_in_triangle(self, point, A, B, C):
        x, y = point
        (x1, y1), (x2, y2), (x3, y3) = A, B, C
        denom = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        if abs(denom) < 1e-10:
            return False
        a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denom
        b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denom
        c = 1 - a - b
        return a >= -1e-10 and b >= -1e-10 and c >= -1e-10

    def __contains__(self, other):
        if not bool(other):
            return True
        if not bool(self):
            return not bool(other)
        A, B, C = self.vertices
        for vertex in other.vertices:
            if not self._point_in_triangle(vertex, A, B, C):
                return False
        return True

    def _segments_intersect(self, p1, p2, q1, q2):
        (x1, y1), (x2, y2) = p1, p2
        (x3, y3), (x4, y4) = q1, q2

        def orientation(px, py, qx, qy, rx, ry):
            val = (qy - py) * (rx - qx) - (qx - px) * (ry - qy)
            if val > 1e-10: return 1
            if val < -1e-10: return -1
            return 0

        o1 = orientation(x1, y1, x2, y2, x3, y3)
        o2 = orientation(x1, y1, x2, y2, x4, y4)
        o3 = orientation(x3, y3, x4, y4, x1, y1)
        o4 = orientation(x3, y3, x4, y4, x2, y2)
        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and self._on_segment(x1, y1, x3, y3, x2, y2):
            return True
        if o2 == 0 and self._on_segment(x1, y1, x4, y4, x2, y2):
            return True
        if o3 == 0 and self._on_segment(x3, y3, x1, y1, x4, y4):
            return True
        if o4 == 0 and self._on_segment(x3, y3, x2, y2, x4, y4):
            return True
        return False

    def _on_segment(self, px, py, qx, qy, rx, ry):
        return (min(px, rx) <= qx <= max(px, rx) and
                min(py, ry) <= qy <= max(py, ry))

    def __and__(self, other):
        if not bool(self) or not bool(other):
            return False
        sides1 = [(self.vertices[i], self.vertices[(i + 1) % 3]) for i in range(3)]
        sides2 = [(other.vertices[i], other.vertices[(i + 1) % 3]) for i in range(3)]
        for s1 in sides1:
            for s2 in sides2:
                if self._segments_intersect(s1[0], s1[1], s2[0], s2[1]):
                    return True
        if self in other or other in self:
            return True
        return False

    def __str__(self):
        return f"Triangle{self.vertices}"

    def __repr__(self):
        return f"Triangle{self.vertices}"


import sys
exec(sys.stdin.read())
