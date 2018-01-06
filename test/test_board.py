"""This file contains the TestBoard class."""
import unittest
import pygame

from src.Board import Board
from src.Scenario import Scenario


class TestBoard(unittest.TestCase):
    """This test class unit tests the Board class."""

    def setUp(self):
        """
        Create a minimal Scenario and use it to create a Board.

        The Scenario is 5x5 (logical size) with the no BeeBot,
        but one Obstacle and Goal.
        """
        # Create the minimal Scenario
        test_scenario = Scenario('Test')
        test_scenario.set_board_step(150)
        test_scenario.set_logical_width(5)
        test_scenario.set_logical_height(8)
        test_scenario.set_background('img/Default/background.jpg')
        test_scenario.add_goal(0, 0)
        test_scenario.add_obstacle(1, 1)

        # Create the test Board
        self.test_board = Board(test_scenario)

    def test_display(self):
        """
        Test the display method of a Board.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test Board
        self.test_board.display(test_screen)


if __name__ == '__main__':
    unittest.main()
