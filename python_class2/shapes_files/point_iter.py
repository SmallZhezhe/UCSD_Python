import math

class Point:
    """Two-dimensional point."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Pretend it is a vector, return magnitude"""
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point({x}, {y})".format(x=self.x, y=self.y)

    def __str__(self):
        """Return pretty string of Point"""
        return "Point at {} and {}".format(self.x, self.y)

"""
from point_iter import Point
p = Point(1, 2)
x, y = p
x
y
for val in p:
    print(val)

q = Point(3, 4)
p = p + q
print(p)
"""
