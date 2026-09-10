#!/usr/bin/env python3
"""Module defining abstract Shape class, Circle, Rectangle, and shape_info."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Base Class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate shape area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate shape perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Voici le code complet pour le fichier `shapes.py` dans le répertoire `python_oop/abc`, suivi d'une explication détaillée ligne par ligne.

---

### Le Code (`shapes.py`)

```python
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
