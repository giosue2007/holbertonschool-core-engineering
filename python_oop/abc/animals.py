#!/usr/bin/env python3
"""Module defining abstract class Animal and its subclasses Dog and Cat."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Base Class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
