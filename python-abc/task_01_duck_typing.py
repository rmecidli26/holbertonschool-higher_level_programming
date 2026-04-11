#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing.
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating ABC and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    Ensures that all subclasses implement area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Concrete class representing a Circle.
    Inherits from Shape.
    """

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle using math.pi."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle using math.pi."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a Rectangle.
    Inherits from Shape.
    """

    def __init__(self, width, height):
        """Initializes Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Uses Duck Typing - calls area() and perimeter() without type checking.
    """
    # Standart format: 'Area: [value]' və 'Perimeter: [value]'
    # Check 8-i keçmək üçün çıxışı tam nəzarətdə saxlayırıq.
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
