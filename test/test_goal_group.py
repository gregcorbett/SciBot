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
        # Create a test sprite list.
        self.sprite_list = [pygame.image.load('img/Default/goal1.jpg')]

        # Create Goals
        self.goal1 = Goal(self.sprite_list, Point(1, 1), 150)
        self.goal2 = Goal(self.sprite_list, Point(2, 2), 150)
        self.goal3 = Goal(self.sprite_list, Point(3, 2), 150)

        # Create a GoalGroup 'ordered' one way
        self.goal_group1 = GoalGroup()
        self.goal_group1.add(self.goal1)
        self.goal_group1.add(self.goal2)

        # Create a GoalGroup 'ordered' the other way
        self.goal_group2 = GoalGroup()
        self.goal_group2.add(self.goal2)
        self.goal_group2.add(self.goal1)

    def test_get_current_goal(self):
        """Test get_current_goal() for ordered and unordered GoalGroups."""
        # Set the test GoalGroup to be ordered.
        self.goal_group1.is_ordered = True
        current_goal = self.goal_group1.get_current_goal()

        self.assertTrue(current_goal.is_equal_to(self.goal1))

        # Now attempt the test with an unordered GoalGroups.
        self.goal_group1.is_ordered = False

        # Calling get_current_goal has no meaning for unordered GoalGroups.
        self.assertRaises(ValueError, self.goal_group1.get_current_goal)

    def test_increment_pointer(self):
        """Test increment_pointer() for ordered and unordered GoalGroups."""
        # Set the test GoalGroup to be ordered.
        self.goal_group1.is_ordered = True

        # Increment the pointer to point at the second Goal.
        self.goal_group1.increment_pointer()

        # Assert the new current goal is the second Goal.
        current_goal = self.goal_group1.get_current_goal()
        self.assertTrue(current_goal.is_equal_to(self.goal2))

        # Now attempt the test with an unordered GoalGroups.
        self.goal_group1.is_ordered = False

        # Calling increment_pointer has no meaning for unordered GoalGroups.
        self.assertRaises(ValueError, self.goal_group1.increment_pointer)

    def test_have_all_goals_been_met(self):
        """Test have_all_goals_been_met returns correctly."""
        # The two Goals start as incomplete.
        # Assert not all the Goals have been met.
        self.assertFalse(self.goal_group1.have_all_goals_been_met())

        # Set one Goal to be met.
        self.goal_group1.components[0].complete()
        # Assert not all the Goals have been completed.
        self.assertFalse(self.goal_group1.have_all_goals_been_met())

        # Set the other Goal to completed.
        self.goal_group1.components[1].complete()
        # Assert all the Goals have been met.
        self.assertTrue(self.goal_group1.have_all_goals_been_met())

    def test_reset_all_goals(self):
        """Test reset_all_goals() for ordered and unordered GoalGroups."""
        # First test the method on ordered GoalGroups.
        self.goal_group1.is_ordered = True

        # Set a Goal to be met
        self.goal_group1.components[0].complete()
        self.goal_group1.components[1].complete()

        # Call reset_all_goals() to reset the Goals.
        self.goal_group1.reset_all_goals()

        # Assert the previously completed Goals are now incomplete.
        self.assertFalse(self.goal_group1.components[1].is_complete)

        # Now test the method on unordered GoalGroups.
        self.goal_group1.is_ordered = False

        # Set a Goal to be met
        self.goal_group1.components[0].complete()
        self.goal_group1.components[1].complete()

        # Call reset_all_goals() to reset the Goals.
        self.goal_group1.reset_all_goals()

        # Assert the previously completed Goals are now incomplete.
        self.assertFalse(self.goal_group1.components[1].is_complete)

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

    def test_is_equal_non_component(self):
        """Check an GoalGroup is different from a non GoalGroup."""
        self.assertFalse(self.goal_group1.is_equal_to(2))


if __name__ == '__main__':
    unittest.main()
