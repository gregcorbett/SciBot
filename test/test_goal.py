"""This file contains the TestGoal class."""
import unittest
import pygame

from src.Goal import Goal
from src.Obstacle import Obstacle
from src.Point import Point


class TestGoal(unittest.TestCase):
    """This test class unit tests the Goal class."""

    def setUp(self):
        """Create a simple Goal for testing."""
        self.test_goal = Goal(["A", "B"], Point(0, 0), 0)

    def test_complete(self):
        """Test that the complete method behaves as expected."""
        # Confirm the Goal is currently incomplete.
        self.assertFalse(self.test_goal.is_complete)
        # Confirm the current value of the Goal's sprite.
        self.assertEqual(self.test_goal.sprite, "A")

        # Call the Goal's complete method.
        self.test_goal.complete()

        # Confirm the Goal is now complete.
        self.assertTrue(self.test_goal.is_complete)
        # Confirm the new value of the Goal's sprite.
        self.assertEqual(self.test_goal.sprite, "B")


    @classmethod
    def test_init(cls):
        """Test the init method of the Goal class."""
        _unused_goal = Goal([None], Point(0, 0), 0)

    def test_is_equal_to(self):
        """Test the is_equal_to_method."""
        # Create a test sprite list.
        goal_sprite_list = [pygame.image.load('img/Default/goal1.jpg')]

        goal = Goal(goal_sprite_list, Point(1, 1), 150)
        # Create a Goal equal to goal
        goal_copy = Goal(goal_sprite_list, Point(1, 1), 150)
        # Create a Goal in a different logical place
        goal_diff_logical_position = Goal(goal_sprite_list, Point(2, 2), 150)
        # Create a Goal that has been completed.
        completed_goal = Goal(goal_sprite_list, Point(1, 1), 150)
        completed_goal.complete()
        # Create a Goal with a different sprite list.
        obstacle_sprite_list = [pygame.image.load('img/Default/obstacle1.jpg')]
        goal_diff_sprite = Goal(obstacle_sprite_list, Point(1, 1), 150)
        # Create an Obstacle, with the same sprite to try and break the test
        obstacle = Obstacle(goal_sprite_list, Point(1, 1), 150)

        # Check that equal goals are infact eqaul
        self.assertTrue(goal.is_equal_to(goal_copy))
        # Check that a goal in a different logical place is not equal
        self.assertFalse(goal.is_equal_to(goal_diff_logical_position))
        # Check an incomplete Goal is not equal to a completed Goal
        self.assertFalse(goal.is_equal_to(completed_goal))
        # Check Goals with different sprites are not equal
        self.assertFalse(goal.is_equal_to(goal_diff_sprite))
        # Check a Goal is not equal to an Obstacle
        self.assertFalse(goal.is_equal_to(obstacle))


if __name__ == '__main__':
    unittest.main()
