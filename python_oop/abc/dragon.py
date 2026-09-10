#!/usr/bin/env python3
"""Module demonstrating mixin classes with SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining SwimMixin, FlyMixin, and its own abilities."""

    def roar(self):
        """Print dragon roaring behavior."""
        print("The dragon roars!")
