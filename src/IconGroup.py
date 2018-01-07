"""This file defines the IconGroup class."""


class IconGroup:
    """This class defines a store for all the Icons used."""

    def __init__(self):
        """Create an empty IconGroup."""
        self.icons = {}  # The underlying Icon objects

    def add(self, icon):
        """Add a Icon to the IconGroup."""
        self.icons[icon.text] = icon

    def display(self, screen):
        """Draw all Icon objects in the IconGroup."""
        for _, icon in self.icons.items():
            icon.display(screen)

    def removal_all(self):
        """Remove all Icons from this IconGroup."""
        self.icons = {}
