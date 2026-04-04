#!/usr/bin/python3
"""Square modülü için Square sınıfını tanımlar."""


class Square:
    """Kareyi tanımlayan sınıf."""

    def __init__(self, size):
        """Yeni bir Square örneği başlatır.

        Args:
            size (int): Karenin boyutu.
        """
        self.__size = size
