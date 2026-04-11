#!/usr/bin/env python3
"""
VerboseList module that extends the built-in list class.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when modified.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list and prints a notification with the count."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item."""
        # pop() metodu index-siz çağırıldıqda sonuncu elementi götürür (-1)
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
