import math

class Point:
    """Two-dimensional point."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Pretend it is a vector from (0, 0), return magnitude"""
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point({x}, {y})".format(x=self.x, y=self.y)

    def __str__(self):
        """Return pretty string of Point"""
        return "Point at {} and {}.".format(self.x, self.y)
