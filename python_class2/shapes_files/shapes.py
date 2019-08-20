"""Shapes module containing 2D Point and Circle"""
import math


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """Pretend it is a vector, return magnitude"""
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        """Return pretty string of Point"""
        return "Point at {} and {}".format(self.x, self.y)

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point(x={}, y={})".format(self.x, self.y)

    def distance(self, other):
        """Return distance between two points."""
        x, y = self.x-other.x, self.y-other.y
        return math.sqrt(x**2 + y**2)

    def __add__(self, other):
        """Return copy of our point, shifted by other point."""
        cls = self.__class__
        return cls(self.x+other.x, self.y+other.y)

    def __mul__(self, value):
        """Return new copy of our point, scaled by given value."""
        cls = self.__class__
        return cls(value*self.x, value*self.y)

    def __rmul__(self, value):
        """Return new copy of our point, scaled by given value."""
        return self.__mul__(value)


class Circle:
    """Circle(radius, point) Keeps record of radius changes"""

    def __init__(self, radius=1, center=None):
        if center is None:
            center = Point()
        self.radius_changes = []
        self.radius = radius
        self.center = center

    @property
    def area(self):
        """Return area of circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Return diameter of circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set radius based on new diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        """Return radius of circle"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set radius of circle. Raises ValueError if negative"""
        if radius < 0:
            raise ValueError("The radius cannot be negative")
        self._radius = radius
        self.radius_changes.append(radius)

    def __repr__(self):
        return f'Circle(radius={self.radius}, center={repr(self.center)})'

"""
from shapes import Circle, Point
p = Point(1,2)
p

q = Point(2, 3)
p + q
p * 3

"""
