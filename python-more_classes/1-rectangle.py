#!/usr/bin/python3



class Rectangle:
    """Dikdörtgeni tanımlayan sınıf."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle örneği başlatır.

        Args:
            width (int): Dikdörtgenin eni.
            height (int): Dikdörtgenin boyu.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width değerini döndürür."""
        return self.__width

    @width.setter
    def width(self, value):
        """width değerini atar ve doğrular."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height değerini döndürür."""
        return self.__height

    @height.setter
    def height(self, value):
        """height değerini atar ve doğrular."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
