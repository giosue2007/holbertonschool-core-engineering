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
