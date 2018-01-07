"""This file contains the TestButtonGroup class."""

import unittest
import pygame
from src.Button import Button
from src.ButtonGroup import ButtonGroup


class TestButtonGroup(unittest.TestCase):
    """This test class unit tests the ButtonGroup class."""

    def setUp(self):
        """Initiate pygame and create a test ButtonGroup and Buttons."""
        # Initiate pygame so we can use fonts
        pygame.init()

        # Create a test ButtonGroup
        self.test_button_group = ButtonGroup()

        # Create some test Buttons
        self.test_button = Button("Test", (0, 0, 0), (255, 255, 255),
                                  (0, 0), (10, 10))
        self.other_button = Button("Other", (0, 0, 0), (255, 255, 255),
                                   (20, 20), (10, 10))

        # Add those test Buttons to the test ButtonGroup
        self.test_button_group.add(self.other_button)
        self.test_button_group.add(self.test_button)

    def test_get_named_button(self):
        """Test the get_named_button method."""
        returned_button = self.test_button_group.get_named_button("Test")

        self.assertIs(self.test_button, returned_button)

    def test_get_pressed_button(self):
        """Test the get_pressed_button method."""
        # Simulate a mouse cick
        position = (5, 5)

        returned_button = self.test_button_group.get_pressed_button(position)

        self.assertIs(self.test_button, returned_button)

        # Simulate a mouse click elswhere, not over a Button
        position = (15, 15)

        returned_button = self.test_button_group.get_pressed_button(position)

        # Because the position is not over a Button,
        # the returned_button should be None
        self.assertIs(returned_button, None)

    def test_unswap_all(self):
        """Test the unswap_all method."""
        button = self.test_button_group.get_named_button("Test")

        button.swap_colours()
        # We could assert that swap_colours() does what we expect.
        # But we trust the test cases for the Button class to do this.

        # Unswap all Buttons
        self.test_button_group.unswap_all()

        self.assertFalse(button.swapped)


if __name__ == '__main__':
    unittest.main()
