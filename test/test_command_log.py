"""This file contains the TestCommandLog class."""

import unittest
import mock
import pygame
from src.CommandLog import CommandLog
from src.CustomEvent import CustomEvent
from src.Point import Point


class TestCommandLog(unittest.TestCase):
    """This test class unit tests the CommandLog class."""

    def setUp(self):
        """Create an empty CommandLog and an example BeeBot memory."""
        # Start pygame as Icons require fonts.
        pygame.init()

        self.test_command_log = CommandLog(Point(0, 0), (25, 5))

        self.beebot_mem = [pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                           pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT),
                           pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT),
                           pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN)]

    def test_update(self):
        """Test update() constructs a CommandLog correctly."""
        self.test_command_log.update(self.beebot_mem)

        for index in self.test_command_log.icons.keys():
            icon = self.test_command_log.icons[index]
            # Check each Icon is 5x5
            self.assertEqual(icon.size, (5, 5))
            # Check each subsequent Icon is 5 pixels
            # to the left of the previous.
            self.assertEqual(icon.screen_location, Point(index * 5, 0))

    # Patch so we can tell if removal_all is called
    @mock.patch('src.IconGroup.IconGroup.removal_all')
    def test_update_do_nothing(self, mock_removal_all):
        """Test update() when no update to the BeeBot memory has occured."""
        # We assume this will work fine
        self.test_command_log.update(self.beebot_mem)

        # This should do nothing
        self.test_command_log.update(self.beebot_mem)

        # Assert removal_all was called exactly once
        # (as part of the first update()).
        self.assertEqual(mock_removal_all.call_count, 1)


if __name__ == '__main__':
    unittest.main()
