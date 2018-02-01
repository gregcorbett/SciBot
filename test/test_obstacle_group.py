"""This file contains the TestObstacleGroup class."""
import unittest
import pygame

from src.Obstacle import Obstacle
from src.ObstacleGroup import ObstacleGroup
from src.Point import Point


class TestObstacleGroup(unittest.TestCase):
    """This test class unit tests the ObstacleGroup class."""

    def setUp(self):
        """Create ObstacleGroups and Obstacles used in testing."""
        # Create a test sprite.
        self.sprite = pygame.image.load('img/Default/obstacle1.jpg')

        # Create Obstacles.
        self.obstacle1 = Obstacle(self.sprite, Point(1, 1), 150)
        self.obstacle2 = Obstacle(self.sprite, Point(2, 2), 150)

        # Create a ObstacleGroup.
        self.obstacle_group1 = ObstacleGroup()
        self.obstacle_group1.add(self.obstacle1)
        self.obstacle_group1.add(self.obstacle2)

    def test_is_equal_non_component(self):
        """Check an ObstacleGroup is different from a non ObstacleGroup."""
        self.assertFalse(self.obstacle_group1.is_equal_to(2))


if __name__ == '__main__':
    unittest.main()
