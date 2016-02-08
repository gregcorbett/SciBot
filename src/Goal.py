"""This file defines the Goal class."""
import pygame


class Goal(pygame.sprite.Sprite):
    """This class defines an individual Goal."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position,  # The starting point of the Goal
                 step):  # Should be the same as the BeeBot step
        """Create a Goal."""
        self.logical_position = start_logical_position

        self.screen_location = start_logical_position.scale(step)

        self.has_been_met = False

        self.sprite = sprite

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    def display(self, screen):
        """Draw the Goal object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, (self.screen_location.x,
                                      self.screen_location.y))
