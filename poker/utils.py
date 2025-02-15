"""
Utility functions for the poker game.

+ This is a good place to put any extra functions you might have that don't need
to be in a class, but are used in multiple places.
"""

import os


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")
