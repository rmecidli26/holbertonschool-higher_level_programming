#!/usr/bin/env python3
"""
Exploring Multiple Inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird.
    Demonstrates multiple inheritance and method overriding.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method from both parents."""
        print("The flying fish lives both in water and the sky!")
