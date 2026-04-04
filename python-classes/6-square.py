#!/usr/bin/python3
"""Square modülü için Square sınıfını tanımlar."""


class Square:
    """Kareyi tanımlayan sınıf."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni bir Square örneği başlatır.

        Args:
            size (int): Karenin boyutu.
            position (tuple): Karenin konumu (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size değerini döndürür."""
        return self.__size

    @size.setter
    def size(self, value):
        """size değerini atar ve doğrular."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position değerini döndürür."""
        return self.__position

    @position.setter
    def position(self, value):
        """position değerini atar ve doğrular."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Karenin alanını döndürür."""
        return self.__size ** 2

    def my_print(self):
        """Kareyi '#' karakteri ve konumuyla ekrana basar."""
        if self.__size == 0:
            print("")
            return

        # Dikey boşluk (position[1])
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Kareyi çiz (yatay boşluk position[0] dahil)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
