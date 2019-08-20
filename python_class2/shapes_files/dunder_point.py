"""Point module consiting of 3-dimensional point code"""
import math


class Point:
    """Three-dimensional point."""

    def __init__(self, xloc=0, yloc=0, zloc=0):
        self.xloc = xloc
        self.yloc = yloc
        self.zloc = zloc

    def shift(self, other):
        """Return copy of our point, shifted by other."""
        return Point(
            self.xloc + other.xloc,
            self.yloc + other.yloc,
            self.zloc + other.zloc
        )

    def scale(self, value):
        """Return new copy of our point, scaled by given value."""
        return Point(
            value * self.xloc,
            value * self.yloc,
            value * self.zloc
        )

    def distance(self, other):
        """Return distance between two points."""
        xloc = self.xloc - other.xloc
        yloc = self.yloc - other.yloc
        zloc = self.zloc - other.zloc
        return math.sqrt(xloc**2 + yloc**2 + zloc**2)

    def __repr__(self):
        """Return dev-readable representation of Point."""
        return "Point({}, {}, {})".format(self.xloc, self.yloc, self.zloc)

    def __add__(self, other):
        """Return new copy of our point, shifted by other."""
        return Point(
            self.xloc + other.xloc,
            self.yloc + other.yloc,
            self.zloc + other.zloc
        )

    def __mul__(self, value):
        """Return new copy of our point, scaled by given value."""
        return Point(
            value * self.xloc,
            value * self.yloc,
            value * self.zloc
        )
