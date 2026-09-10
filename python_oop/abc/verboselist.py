#!/usr/bin/env python3
"""Module defining VerboseList extending the built-in list class."""


class VerboseList(list):
    """List subclass that prints notification messages on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with items from iterable and print a notification."""
        items_count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list at index and print a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
