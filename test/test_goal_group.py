"""This file contains the TestGoalGroup class."""
import unittest
import pygame

from src.Goal import Goal
from src.GoalGroup import GoalGroup
from src.Point import Point


class TestGoalGroup(unittest.TestCase):
    """This test class unit tests the GoalGroup class."""

    def setUp(self):
        """Create GoalGroups and Goals used in testing."""
        # Create a test sprite
        sprite = pygame.image.load('img/Default/goal1.jpg')

        # Create Goals
        self.goal1 = Goal(sprite, Point(1, 1), 150)
        self.goal2 = Goal(sprite, Point(2, 2), 150)
        self.goal3 = Goal(sprite, Point(3, 2), 150)

        # Create a GoalGroup 'ordered' one way
        self.goal_group1 = GoalGroup()
        self.goal_group1.add(self.goal1)
        self.goal_group1.add(self.goal2)

        # Create a GoalGroup 'ordered' the other way
        self.goal_group2 = GoalGroup()
        self.goal_group2.add(self.goal2)
        self.goal_group2.add(self.goal1)

    def test_is_equal_to_eq_unord(self):
        """Test two equal unordered GoalGroups for equality."""
        # Set the GoalGroups to unordered
        self.goal_group1.is_ordered = False
        self.goal_group2.is_ordered = False

        self.assertTrue(self.goal_group1.is_equal_to(self.goal_group2),
                        "Two equal unordered GoalGroups are not equal.")

    def test_is_equal_to_eq_ord(self):
        """Test two equal ordered GoalGroups for equality."""
        # Set the GoalGroups to ordered
        self.goal_group1.is_ordered = True
        self.goal_group2.is_ordered = True

        self.assertFalse(self.goal_group1.is_equal_to(self.goal_group2),
                         "Two unequal ordered GoalGroups are equal.")

    def test_is_equal_to_mixed_order(self):
        """Test two mixed ordered GoalGroups for equality."""
        # Set the GoalGroups so one is ordered and one is unordered
        self.goal_group1.is_ordered = True
        self.goal_group2.is_ordered = False

        self.assertFalse(self.goal_group1.is_equal_to(self.goal_group2),
                         "A ordered and unordered GoalGroup are equal.")

    def test_is_equal_to_uneq_unord(self):
        """Test two unequal GoalGroups for equality."""
        # Create a unequal GoalGroup
        unequal_goal_group = GoalGroup()
        unequal_goal_group.add(self.goal2)
        unequal_goal_group.add(self.goal3)

        # Set the GoalGroups to unordered.
        self.goal_group1.is_ordered = False
        unequal_goal_group.is_ordered = False

        self.assertFalse(self.goal_group1.is_equal_to(unequal_goal_group),
                         "Unequal GoalGroups are equal.")

    def test_is_equal_to_uneq_ord(self):
        """Test two unequal GoalGroups for equality."""
        # Create a unequal GoalGroup
        unequal_goal_group = GoalGroup()
        unequal_goal_group.add(self.goal2)
        unequal_goal_group.add(self.goal3)

        # Set the GoalGroups to ordered.
        self.goal_group1.is_ordered = True
        unequal_goal_group.is_ordered = True

        self.assertFalse(self.goal_group1.is_equal_to(unequal_goal_group),
                         "Unequal GoalGroups are equal.")

    def test_is_equal_to_uneq_larger(self):
        """Test two differently sized GoalGroups for equality."""
        # Create a larger GoalGroup
        larger_goal_group = GoalGroup()
        larger_goal_group.add(self.goal1)
        larger_goal_group.add(self.goal2)
        larger_goal_group.add(self.goal3)

        # Set the GoalGroups to ordered
        self.goal_group1.is_ordered = True
        larger_goal_group.is_ordered = True

        self.assertFalse(self.goal_group1.is_equal_to(larger_goal_group),
                         "Different sized GoalGroups are equal.")


if __name__ == '__main__':
    unittest.main()
