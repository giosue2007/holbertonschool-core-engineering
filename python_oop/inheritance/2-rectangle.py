#!/usr/bin/env python3
"""Rectangle class module inheriting from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height after validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
