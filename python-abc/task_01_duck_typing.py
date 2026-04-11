#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing module.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """Initializes circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle: PI * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle: 2 * PI * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter using Duck Typing.
    It doesn't check the type, it just calls the methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
