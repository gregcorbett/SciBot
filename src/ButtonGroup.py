"""This file defines the ButtonGroup class."""
import pygame


class ButtonGroup:
    """This class defines a store for all the Buttons used."""

    def __init__(self):
        """Create an empty ButtonGroup."""
        self.buttons = {}  # The underlying Goal objects

    def add(self, key, button):
        """Add a Button to the ButtonGroup."""
        self.buttons[key] = button

    def display(self, screen):
        """Draw all Button objects in the ButtonGroup."""
        for key, button in self.buttons.items():
            button.display(screen)

    def get_appropriate_button_name(self, mouse_position):
        """Return the pressed Button name."""
        for key, button in self.buttons.items():
            if button.is_mouse_over_button(mouse_position):
                return key
