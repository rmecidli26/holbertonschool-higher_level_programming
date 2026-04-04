#!/usr/bin/python3
"""Square modülü için Square sınıfını tanımlar."""


class Square:
    """Kareyi tanımlayan sınıf."""

    def __init__(self, size=0):
        """Yeni bir Square örneği başlatır.

        Args:
            size (int): Karenin boyutu (varsayılan 0).

        Raises:
            TypeError: size tam sayı değilse.
            ValueError: size 0'dan küçükse.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Karenin alanını hesaplar ve döndürür.

        Returns:
            int: Karenin alanı (size * size).
        """
        return self.__size ** 2
