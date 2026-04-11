#!/usr/bin/env python3
"""
Module for Shapes and Duck Typing.
Contains Shape, Circle, Rectangle classes and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class implementation."""

    def __init__(self, radius):
        """Initializes Circle with radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class implementation."""

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
    Prints shape information using Duck Typing.
    Calls area() and perimeter() directly.
    """
    # Check 8 (Output) üçün: İki sətir arasında və ya sonunda 
    # artıq boşluq qalmadığından əmin olmaq üçün .format() ən yaxşısıdır.
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
