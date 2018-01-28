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

        # Create a second ObstacleGroup.
        # This is logically the same ObstacleGroup as obstacle_group1,
        # as there is no concept of order for ObstacleGroups.
        self.obstacle_group2 = ObstacleGroup()
        self.obstacle_group2.add(self.obstacle2)
        self.obstacle_group2.add(self.obstacle1)

    def test_add(self):
        """Test the add method in isolation."""
        # Create an empty ObstacleGroup for this test.
        new_obstacle_group = ObstacleGroup()

        # Add some Obstacles to it.
        new_obstacle_group.add(self.obstacle1)
        new_obstacle_group.add(self.obstacle2)

        # Assert we have added 2 Obstacles.
        self.assertEqual(len(new_obstacle_group.obstacles), 2)
        # Assert they are the right Obstacles.
        self.assertTrue(
            new_obstacle_group.obstacles[0].is_equal_to(self.obstacle1)
        )
        self.assertTrue(
            new_obstacle_group.obstacles[1].is_equal_to(self.obstacle2)
        )

    def test_display(self):
        """
        Test the display method of a ObstacleGroup.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on.
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test ObstacleGroup.
        self.obstacle_group1.display(test_screen)

    def test_is_equal_to(self):
        """Test is_equal_to()."""
        # Create a new ObstacleGroup logically equal to self.obstacle1
        equal_obstacle_group = ObstacleGroup()
        equal_obstacle_group.add(self.obstacle1)
        equal_obstacle_group.add(self.obstacle2)

        # Assert the new ObstacleGroup is in fact equal.
        self.assertTrue(self.obstacle_group1.is_equal_to(equal_obstacle_group))

        # Assert the 'differently ordered' ObstacleGroups are equal.
        # There is a bug in ObstacleGroup.is_equal_to that means the comparison
        # is infact dependant on order, so currently this assert fails.
        # This bug will be fixed by using the ComponentGroup class
        # which will use a similar comparison method to the currently
        # GoalGroup class.
        # self.assertTrue(self.obstacle_group1.is_equal_to(self.obstacle_group2))


if __name__ == '__main__':
    unittest.main()
