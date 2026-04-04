#!/usr/bin/python3
"""
Bu modul Rectangle sinfini təyin edir.
Obyekt silindikdə mesaj çap edən __del__ metodu daxildir.
"""


class Rectangle:
    """Düzbucaqlını təmsil edən sinif."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle obyekti yaradır."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width üçün getter metodu."""
        return self.__width

    @size.setter # Qeyd: 4-cü tapşırıqdakı setter məntiqi qorunur
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
        """Sahəni qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimetri qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlının '#' ilə vizual təsvirini qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for i in range(self.__height):
            rect_str += ("#" * self.__width)
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Obyektin yenidən yaradılması üçün lazım olan sətri qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silindikdə mesaj çap edir."""
        print("Bye rectangle...")
