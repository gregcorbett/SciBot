"""This file defines the Board class."""
import pygame
from src.Component import Component
from src.Point import Point


class Board(Component):
    """This class defines the board (a.k.a. map)."""

    def __init__(self, scenario):
        """Create the board."""
        self.step = scenario.get_board_step()

        # Call superclass constructor
        super().__init__(scenario.get_background(),
                         Point(0, 0),  # This is the window topleft corner
                         self.step)

        # Work out (and check) screen size, also store for
        # checking the BeeBot has not fallen of the edge
        self.logical_board_height = scenario.get_logical_height()
        self.logical_board_width = scenario.get_logical_width()

        # Board dimensions in terms of pixels
        self.board_height = self.logical_board_height * self.step
        self.board_width = self.logical_board_width * self.step

        self.border_colour = scenario.get_border_colour()

        self.obstacle_group = scenario.get_obstacle_group()

        self.goal_group = scenario.get_goal_group()

        # Need to check the Board pixel height matches the image pixel height
        if self.board_height != self.sprite.get_height():
            raise ValueError(("Error 1: board height does "
                              "not match image height.\n"
                              "Board Height = %s\n"
                              "Image Height = %s"
                              % (self.board_height,
                                 self.sprite.get_height())))

        # Need to check the Board pixel width matches the image pixel width
        if self.board_width != self.sprite.get_width():
            raise ValueError(("Error 2: board width does "
                              "not match image width.\n"
                              "Board Width = %s\n"
                              "Image Width = %s"
                              % (self.board_width,
                                 self.sprite.get_width())))

        # Need to check the pixel height is a multiple of step
        if self.board_height % self.step != 0:
            raise ValueError(("Error 3: height mod step != 0.\n"
                              "Height = %s\n"
                              "Step   = %s" % (self.board_height,
                                               self.step)))

        # Need to check the pixel height is a multiple of step
        if self.board_width % self.step != 0:
            raise ValueError(("Error 4: width mod step != 0.\n"
                              "Width = %s\n"
                              "Step  = %s" % (self.board_width,
                                              self.step)))

    def display(self, screen):
        """Display the board on screen."""
        # Call the superclass display method
        super().display(screen)
        self.obstacle_group.display(screen)
        self.goal_group.display(screen)

        # Draw lines over Board background image
        if self.border_colour is not None:
            for iter_width in range(0, self.board_width + 1, self.step):
                pygame.draw.line(screen,
                                 self.border_colour,
                                 (iter_width, 0),
                                 (iter_width, self.board_height),
                                 5)

            for iter_height in range(0, self.board_height + 1, self.step):
                pygame.draw.line(screen,
                                 self.border_colour,
                                 (0, iter_height),
                                 (self.board_width, iter_height),
                                 5)

    def is_equal_to(self, other_component):
        """Compare this Board for equality with other_component."""
        if not isinstance(other_component, Board):
            # An Board can obviously never be equal to a non Board
            return False
        # Comparing a Board to another Board has not yet been implemented
        raise NotImplementedError()
