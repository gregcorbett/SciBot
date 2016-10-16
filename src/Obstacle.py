"""This file defines the Object class."""
import pygame


class Obstacle(pygame.sprite.Sprite):
    """This class defines an individual Obstacle."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position,  # The starting point of the Obstacle
                 step):  # Should be the same as the BeeBot step

        """Create a Obstacle."""
        # The position of the Goal in terms of squares on the screen
        self.logical_position = start_logical_position

        # The position of the Goal in terms pixels
        self.screen_location = start_logical_position.scale(step)

        # The sprite to display on screen for this Goal
        self.sprite = sprite

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    def display(self, screen):
        """Draw the Obstacle object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, (self.screen_location.x,
                                      self.screen_location.y))
