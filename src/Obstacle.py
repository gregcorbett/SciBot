"""This file defines the Object class."""
import pygame


class Obstacle(pygame.sprite.Sprite):
    """This class defines an individual Obstacle."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position_x,  # The starting x of the Obstacle
                 start_logical_position_y,  # The starting y of the Obstacle
                 step):  # Should be the same as the BeeBot step
        """Create a Obstacle."""
        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

        self.screen_location_x = start_logical_position_x * step
        self.screen_location_y = start_logical_position_y * step

        self.sprite = sprite

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    def display(self, screen):
        """Draw the Obstacle object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, (self.screen_location_x,
                                      self.screen_location_y))
