#!/usr/bin/env python3
"""
Module task_01_duck_typing
Provides classes for geometric shapes and a function to display their info.
Demonstrates Abstract Base Classes (ABC) and Duck Typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class for all geometric shapes.
    Requires implementation of area and perimeter methods.
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
    Circle class that inherits from Shape.
    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """Initializes Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle using math.pi."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle using math.pi."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
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
    This function uses Duck Typing: it calls area() and perimeter()
    without checking if the object is an instance of Shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
