#!/usr/bin/env python3
"""
CountedIterator module that tracks the number of iterations.
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable object.
        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current number of items that have been iterated."""
        return self.count

    def __next__(self):
        """
        Increments the counter and returns the next item from the iterator.
        Raises StopIteration if there are no more items.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # Əgər orijinal iterator bitibsə, StopIteration xətasını ötürürük
            raise StopIteration

    def __iter__(self):
        """Allows the CountedIterator to be used in loops."""
        return self
