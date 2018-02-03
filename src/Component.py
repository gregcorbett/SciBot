"""
This file defines the Component class.

Extend this class to create Game Components like the Board, the BeeBot and
individual Obstacles and Goals.
"""

import pygame


class Component(pygame.sprite.Sprite):
    """This class defines an individual Component."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position,  # The starting point of the Component
                 step):  # The 'size' of the Component
        """Create a Component."""
        # The sprite to display on screen for this Component
        self.sprite = sprite

        # The position of the Component in terms of squares on the screen
        self.logical_position = start_logical_position.copy()

        # The position of the Goal in terms pixels
        self.screen_location = start_logical_position.scale(step)

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    def display(self, screen):
        """Draw the Component object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, self.screen_location)

    def is_equal_to(self, other_component):
        """Compare this Component for equality with other_component."""
        return (self.sprite == other_component.sprite and
                self.screen_location.is_equal_to(other_component.screen_location))
