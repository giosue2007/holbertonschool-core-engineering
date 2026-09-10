#!/usr/bin/env python3
"""Square class module inheriting from Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with size using the Rectangle parent class."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
