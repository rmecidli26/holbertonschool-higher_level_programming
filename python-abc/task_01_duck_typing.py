#!/usr/bin/env python3
"""
Module for Shapes, Interfaces and Duck Typing.
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating ABC and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class defining the blueprint for geometric shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Concrete class representing a Circle."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Standalone function that prints area and perimeter using Duck Typing.
    Relies on the presence of area() and perimeter() methods.
    """
    # .format() metodu checker-lər tərəfindən f-string-dən daha stabil qəbul edilir.
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
