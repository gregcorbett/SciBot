"""This file defines the Goal class."""
import pygame


class Goal(pygame.sprite.Sprite):
    """This class defines an individual Goal."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position,  # The positon of the Goal
                 step):  # Should be the same as the BeeBot step
        """Create a Goal."""
        # The position of the Goal in terms of squares on the screen
        self.logical_position = start_logical_position

        # The position of the Goal in terms pixels
        self.screen_location = start_logical_position.scale(step)

        # True if Goal has been met
        self.has_been_met = False

        # The sprite to display on screen for this Goal
        self.sprite = sprite

        # calling superclass constructor
        pygame.sprite.Sprite.__init__(self)

    def display(self, screen):
        """Draw the Goal object on screen, if it has a sprite."""
        if self.sprite is not None:
            screen.blit(self.sprite, (self.screen_location.x,
                                      self.screen_location.y))

    def is_equal_to(self, other_goal):
        """Compare this Goal for equality with other_goal."""
        return (self.sprite == other_goal.sprite and
                self.has_been_met == other_goal.has_been_met and
                self.screen_location.is_equal_to(other_goal.screen_location))
