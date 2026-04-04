#!/usr/bin/python3
"""
Bu modul Rectangle sinfini təyin edir.
Sahə və perimetr hesablama metodlarını daxil edir.
"""


class Rectangle:
    """Düzbucaqlını təmsil edən sinif."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle obyekti yaradır.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width üçün getter metodu."""
        return self.__width

    @width.setter
    def width(self, value):
        """width üçün setter metodu."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height üçün getter metodu."""
        return self.__height

    @height.setter
    def height(self, value):
        """height üçün setter metodu."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Düzbucaqlının sahəsini (width * height) qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır.
        Əgər en və ya hündürlük 0-dırsa, 0 qaytarır.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
