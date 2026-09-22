#!/usr/bin/env python3
"""
Module containing the append_write function.
"""


def append_write(filename="", text=""):
    """Appends string to text file (UTF8) and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
