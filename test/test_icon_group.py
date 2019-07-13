"""This file contains the TestIconGroup class."""

import unittest
import pygame
from src.Icon import Icon
from src.IconGroup import IconGroup


class TestIconGroup(unittest.TestCase):
    """This test class unit tests the IconGroup class."""

    def setUp(self):
        """Initiate pygame and create a test IconGroup and Icons."""
        # Initiate pygame so we can use fonts
        pygame.init()

        # Create a test IconGroup
        self.test_icon_group = IconGroup()

        # Create some test Icons
        self.test_icon = Icon("Test", (0, 0, 0), (255, 255, 255),
                              (0, 0), (10, 10))
        self.other_icon = Icon("Other", (0, 0, 0), (255, 255, 255),
                               (20, 20), (10, 10))

        # Add those test Icons to the test IconGroup
        self.test_icon_group.add(self.other_icon)
        self.test_icon_group.add(self.test_icon)

    def test_add(self):
        """
        Test the add method when it uses a specific key.

        The default key behaviour is tested indirectly in setUp().
        """
        new_icon = Icon("New", (0, 0, 0), (255, 255, 255),
                        (30, 30), (10, 10))

        # Add new_icon to the test_icon_group, but use a specific key.
        self.test_icon_group.add(new_icon, key="Old")

        # Assert the new_icon was stored under the correct key.
        self.assertIs(self.test_icon_group.icons["Old"], new_icon)
        # Assert that there is nothing stored under the "New" key,
        # which is what would happen if new_icon
        # was added with no specific key.
        self.assertFalse("New" in self.test_icon_group.icons.keys())

    def test_display(self):
        """
        Test the display method of a IconGroup.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test IconGroup
        self.test_icon_group.display(test_screen)

    def test_removal_all(self):
        """Test the removal_all method."""
        self.test_icon_group.removal_all()

        self.assertEqual(self.test_icon_group.icons, {})


if __name__ == '__main__':
    unittest.main()
