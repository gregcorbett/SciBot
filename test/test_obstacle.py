"""This file contains the TestObstacle class."""
import unittest
import pygame

from src.Goal import Goal
from src.Obstacle import Obstacle
from src.Point import Point


class TestObstacle(unittest.TestCase):
    """This test class unit tests the Obstacle class."""

    def test_is_equal_to(self):
        """Test the is_equal_to_method."""
        # Create a test sprite
        obstacle_sprite_list = [pygame.image.load('img/Default/obstacle1.jpg')]
        goal_sprite_list = [pygame.image.load('img/Default/goal1.jpg')]

        obstacle = Obstacle(obstacle_sprite_list, Point(1, 1), 150)
        # Create a Obstacle equal to obstacle
        obstacle_copy = Obstacle(obstacle_sprite_list, Point(1, 1), 150)
        # Create a Obstacle in a different logical place
        obstacle_diff_logical_position = Obstacle(obstacle_sprite_list,
                                                  Point(2, 2), 150)
        # Create a Obstacle with a different sprite
        obstacle_diff_sprite = Obstacle(goal_sprite_list, Point(1, 1), 150)
        # Create an Goal, with the same sprite to try and break the test
        goal = Goal(obstacle_sprite_list, Point(1, 1), 150)

        # Check that equal Obstacles are infact eqaul
        self.assertTrue(obstacle.is_equal_to(obstacle_copy))
        # Check that a Obstacles in a different logical place is not equal
        self.assertFalse(obstacle.is_equal_to(obstacle_diff_logical_position))
        # Check an Obstacle with a different Sprite is not equal
        self.assertFalse(obstacle.is_equal_to(obstacle_diff_sprite))
        # Check a Obstacle is not equal to an Goal
        self.assertFalse(obstacle.is_equal_to(goal))


if __name__ == '__main__':
    unittest.main()
