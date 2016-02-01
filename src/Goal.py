"""This file defines the Goal class."""
from pygame.sprite import Sprite


class Goal(Sprite):
    """This class defines an individual Goal."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position_x,  # The starting x of the Goal
                 start_logical_position_y,  # The starting y of the Goal
                 step):  # Should be the same as the BeeBot step
        """Create a Goal."""
        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

        self.screen_location_x = start_logical_position_x * step
        self.screen_location_y = start_logical_position_y * step

        self.has_been_met = False
        
        self.sprite = sprite

        # calling superclass constructor
        Sprite.__init__(self)

    def display(self, screen):
        """Draw the Goal object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, (self.screen_location_x,
                                      self.screen_location_y))
