"""This file defines the Board class."""
import pygame


class Board:
    """This class defines the board (a.k.a. map)."""

    def __init__(self, scenario):
        """Create the board."""
        self.step = scenario.get_element('BoardStep')

        # Only need these to work out (and check) screen size
        logical_board_height = scenario.get_element('LogicalHeight')
        logical_board_width = scenario.get_element('LogicalWidth')

        self.board_height = logical_board_height * self.step
        self.board_width = logical_board_width * self.step

        self.background_image = scenario.get_element('Background')

        self.border_colour = scenario.get_element('BorderColour')

        self.obstacle_group = scenario.get_element('ObstacleGroup')

        self.goal_group = scenario.get_element('GoalGroup')

        if self.board_height != self.background_image.get_height():
            print("Error 1: board height does not match image height")
            print("Board Height = ", self.board_height)
            print("Image Height = ", self.background_image.get_height())
            exit()

        if self.board_width != self.background_image.get_width():
            print("Error 2: board width does not match image width")
            print("Board Width = ", self.board_width)
            print("Image Width = ", self.background_image.get_width())
            exit()

        if self.board_height % self.step != 0:
            print("Error 3: height % step != 0")
            print("Height = ", self.board_height)
            print("Step   = ", self.step)
            exit()

        if self.board_width % self.step != 0:
            print("Error 4: width % step != 0")
            print("Width = ", self.board_width)
            print("Step  = ", self.step)
            exit()

    def display(self, screen):
        """Display the board on screen."""
        screen.blit(self.background_image, (0, 0))
        self.obstacle_group.display(screen)
        self.goal_group.display(screen)

        if self.border_colour is not None:
            for iter_width in range(0, self.board_width, self.step):
                pygame.draw.line(screen,
                                 self.border_colour,
                                 (iter_width, 0),
                                 (iter_width, self.board_height),
                                 5)

            for iter_height in range(0, self.board_height, self.step):
                pygame.draw.line(screen,
                                 self.border_colour,
                                 (0, iter_height),
                                 (self.board_width, iter_height),
                                 5)
