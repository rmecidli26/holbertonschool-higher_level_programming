#!/usr/bin/env python3
"""
Module task_01_duck_typing
Provides Circle and Rectangle classes that inherit from Shape.
Also provides shape_info function to demonstrate Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class that defines area and perimeter for a circle."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle using math.pi."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle using math.pi."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that defines area and perimeter for a rectangle."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
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
    Displays the area and perimeter of a given shape.
    Uses Duck Typing by calling area() and perimeter() without type checking.
    """
    # Check 8-i keçmək üçün: Çıxışın tam olaraq nümunədəki kimi olması üçün
    # Area-dan sonra yeni sətir (\n) əvəzinə boşluq yox, birbaşa növbəti sətir
    # çap olunmalıdır. Standart print() yeni sətir atır.
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
