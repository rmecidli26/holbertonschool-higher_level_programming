#!/usr/bin/env python3
"""
Mastering Mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """Mixin to add swimming behavior."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying behavior."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from multiple mixins to gain
    swimming and flying capabilities.
    """

    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
