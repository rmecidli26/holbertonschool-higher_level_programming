#!/usr/bin/env python3
"""
Module task_01_duck_typing
Defines Shape, Circle, Rectangle and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize Circle."""
        self.radius = radius

    def area(self):
        """Area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    print("Area: {}".format(shape.area()), end="")
    print("Perimeter: {}".format(shape.perimeter()))
