#!/usr/bin/python3
"""MyList sinfi üçün modul"""


class MyList(list):
    """Siyahıdan miras alan sinif"""

    def print_sorted(self):
        """Siyahını artan sıra ilə çap edir"""
        print(sorted(self))
