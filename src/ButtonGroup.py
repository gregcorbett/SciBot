"""This file defines the ButtonGroup class."""

from src.IconGroup import IconGroup


class ButtonGroup(IconGroup):
    """This class defines a store for all the Buttons used."""

    def get_named_button(self, button_name):
        """Return the named Button."""
        return self.icons[button_name]

    def get_pressed_button(self, mouse_position):
        """Return the pressed Button."""
        for _, button in self.icons.items():
            if button.is_mouse_over_button(mouse_position):
                return button
        return None

    def unswap_all(self):
        """Unswap all Buttons where swapped equals True."""
        for _, button in self.icons.items():
            if button.swapped:
                button.swap_colours()
