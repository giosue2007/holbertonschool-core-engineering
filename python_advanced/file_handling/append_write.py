#!/usr/bin/env python3
"""
Module containing the append_write function.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
