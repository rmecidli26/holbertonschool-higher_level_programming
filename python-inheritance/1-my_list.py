#!/usr/bin/python3
"""MyList sinfi üçün modul"""


class MyList(list):
    """Siyahıdan miras alan sinif"""

    def print_sorted(self):
        """Yalnız müsbət tam ədədləri sıralayıb çap edir"""
        # Siyahıdakı elementlərdən mənfi olmayanları süzgəcdən keçiririk
        positives = [x for x in self if isinstance(x, int) and x >= 0]
        print(sorted(positives))
