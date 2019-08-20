import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return "Point at ({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "Point(x={}, y={})".format(self.x, self.y)


"""
from shapes import Point
p = Point(1, 2)
p.magnitude

q = Point(3, 4)
q.magnitude
Operator Overloading

"""


class Circle:
    """Class to create Circle objects"""
    def __init__(self, radius=1):
        self.radius = radius

    @classmethod
    def from_area(cls, area):
        return cls(math.sqrt(area / math.pi))

    @staticmethod
    def is_valid_radius(radius):
        return radius > 0

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


"""
from shapes import Circle
c = Circle()
c.diameter
c.diameter = 3
c.radius

Exam questions:
>>> c = Circle(2)
>>> c.diameter
4
>>> c.radius
2
>>> c.area
12.566370614359172
>>> c.diameter = 5
>>> c.radius
2.5
>>> c.area
19.634954084936208
>>>

"""


class GreetName:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print("Hello {name}".format(name=self.name))
