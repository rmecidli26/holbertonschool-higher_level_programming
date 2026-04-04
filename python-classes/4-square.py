#!/usr/bin/python3
"""Square modülü için Square sınıfını tanımlar."""


class Square:
    """Kareyi tanımlayan sınıf."""

    def __init__(self, size=0):
        """Yeni bir Square örneği başlatır.

        Args:
            size (int): Karenin boyutu (varsayılan 0).
        """
        self.size = size

    @property
    def size(self):
        """size değerini döndürür (Getter)."""
        return self.__size

    @size.setter
    def size(self, value):
        """size değerini atar ve doğrular (Setter).

        Args:
            value (int): Atanacak yeni boyut.

        Raises:
            TypeError: value tam sayı değilse.
            ValueError: value 0'dan küçükse.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Karenin alanını hesaplar ve döndürür.

        Returns:
            int: Karenin alanı.
        """
        return self.__size ** 2
