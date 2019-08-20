"""A more pythonic version of Point class"""
import math


class Point:

    """Three-dimensional point."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def magnitude(self):
        """Pretend it is a vector, return magnitude"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, other):
        """Return distance between two points."""
        x, y, z = (self.x-other.x), (self.y-other.y), (self.z-other.z)
        return math.sqrt(x**2 + y**2 + z**2)

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        cls = self.__class__
        return cls(self.x+other.x, self.y+other.y, self.z+other.z)

    def __mul__(self, value):
        """Return new copy of our point, scaled by given value."""
        cls = self.__class__
        return cls(value*self.x, value*self.y, value*self.z)

    def __rmul__(self, value):
        """Return new copy of our point, scaled by given value."""
        return self.__mul__(value)

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "{cls}({x}, {y}, {z})".format(
            cls=self.__class__.__name__,
            x=self.x,
            y=self.y,
            z=self.z,
        )

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y and self.z==other.z
