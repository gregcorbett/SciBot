"""
This file defines the Component class.

Extend this class to create Game Components like the Board, the BeeBot and
individual Obstacles and Goals.
"""

import pygame


class Component(pygame.sprite.Sprite):
    """This class defines an individual Component."""

    def __init__(self,
                 sprite_list,  # The list of sprites to display.
                 start_logical_position,  # The starting point of the Component
                 step):  # The 'size' of the Component
        """Create a Component."""
        # The sprite(s) to display on screen for this Component.
        self._sprite_list = sprite_list

        # Which sprite in self._sprite_list to display.
        self._sprite_list_index = 0

        # The position of the Component in terms of squares on the screen
        self.logical_position = start_logical_position.copy()

        # The position of the Goal in terms pixels
        self.screen_location = start_logical_position.scale(step)

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    @property
    def sprite(self):
        """A "public" getter for the current sprite."""
        return self._sprite_list[self._sprite_list_index]

    @sprite.setter
    def sprite(self, new_sprite):
        """
        A "public" getter for the current sprite.

        This method is needed for Components that rotate, like the BeeBot.
        """
        self._sprite_list[self._sprite_list_index] = new_sprite

    @property
    def sprite_list(self):
        """A "public" getter for self._sprite_list."""
        return self._sprite_list

    @property
    def sprite_list_index(self):
        """A "public" getter for self._sprite_list_index."""
        return self._sprite_list_index

    def increment_sprite(self):
        """Increment the sprite to display for this Component."""
        if self._sprite_list_index < len(self._sprite_list) - 1:
            self._sprite_list_index = self._sprite_list_index + 1

    def display(self, screen):
        """Draw the Component object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, self.screen_location)

    def is_equal_to(self, other_component):
        """Compare this Component for equality with other_component."""
        return (self.sprite_list == other_component.sprite_list and
                self.sprite_list_index == other_component.sprite_list_index and
                self.screen_location.is_equal_to(other_component.screen_location))
