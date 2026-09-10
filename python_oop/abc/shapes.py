#!/usr/bin/env python3
"""Module implementing abstract shape classes and duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to compute shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute shape perimeter."""
        pass


class Circle(Shape):
    """Circle shape implementation."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate and return area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return perimeter (circumference) of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using Duck Typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
