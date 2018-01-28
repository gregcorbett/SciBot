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
        self.sprite = pygame.image.load('img/Default/goal1.jpg')

        # Create Goals
        self.goal1 = Goal(self.sprite, Point(1, 1), 150)
        self.goal2 = Goal(self.sprite, Point(2, 2), 150)
        self.goal3 = Goal(self.sprite, Point(3, 2), 150)

        # Create a GoalGroup 'ordered' one way
        self.goal_group1 = GoalGroup()
        self.goal_group1.add(self.goal1)
        self.goal_group1.add(self.goal2)

        # Create a GoalGroup 'ordered' the other way
        self.goal_group2 = GoalGroup()
        self.goal_group2.add(self.goal2)
        self.goal_group2.add(self.goal1)

    def test_add(self):
        """Test the add method in isolation."""
        # Create an empty GoalGroup for this test.
        new_goal_group = GoalGroup()

        # Add some Goals to it.
        new_goal_group.add(self.goal1)
        new_goal_group.add(self.goal2)

        # Assert we have added 2 goals.
        self.assertEqual(len(new_goal_group.goals), 2)
        # Assert they are the right goals.
        self.assertTrue(new_goal_group.goals[0].is_equal_to(self.goal1))
        self.assertTrue(new_goal_group.goals[1].is_equal_to(self.goal2))

    def test_display(self):
        """
        Test the display method of a GaolGroup.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on.
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test GoalGroup.
        self.goal_group1.display(test_screen)

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
        # Set the two Goals to be not met.
        self.goal_group1.goals[0].has_been_met = False
        self.goal_group1.goals[1].has_been_met = False
        # Assert not all the Goals have been met.
        self.assertFalse(self.goal_group1.have_all_goals_been_met())

        # Set one Goal to be met.
        self.goal_group1.goals[0].has_been_met = True
        self.goal_group1.goals[1].has_been_met = False
        # Assert not all the Goals have been met.
        self.assertFalse(self.goal_group1.have_all_goals_been_met())

        # Set both Goals to be met.
        self.goal_group1.goals[0].has_been_met = True
        self.goal_group1.goals[1].has_been_met = True
        # Assert all the Goals have been met.
        self.assertTrue(self.goal_group1.have_all_goals_been_met())

    def test_reset_all_goals(self):
        """Test reset_all_goals() for ordered and unordered GoalGroups."""
        # First test the method on ordered GoalGroups.
        self.goal_group1.is_ordered = True

        # Set a Goal to be met
        self.goal_group1.goals[0].has_been_met = False
        self.goal_group1.goals[1].has_been_met = True

        # Call reset_all_goals() to reset the Goals.
        self.goal_group1.reset_all_goals()

        # Assert the previously met Goals are now un met.
        self.assertFalse(self.goal_group1.goals[1].has_been_met)

        # Now test the method on unordered GoalGroups.
        self.goal_group1.is_ordered = False

        # Set a Goal to be met
        self.goal_group1.goals[0].has_been_met = False
        self.goal_group1.goals[1].has_been_met = True

        # Call reset_all_goals() to reset the Goals.
        self.goal_group1.reset_all_goals()

        # Assert the previously met Goals are now un met.
        self.assertFalse(self.goal_group1.goals[1].has_been_met)

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

    def test_is_equal_to_same_goal(self):
        """
        Test logically equal GoalGroups for equality.

        This particular test case catches when the underlying objects
        are different but the GoalGroups are the same.
        """
        # same_goal1 is a different python object to self.goal1,
        # but logically are the same. The same is true for same_goal2.
        same_goal1 = Goal(self.sprite, Point(1, 1), 150)
        same_goal2 = Goal(self.sprite, Point(2, 2), 150)

        # goal_groupA is a different python object to self.goal_group1,
        # but logically are the same.
        same_goal_group = GoalGroup()
        same_goal_group.add(same_goal1)
        same_goal_group.add(same_goal2)

        # Set both GoalGroups to be un ordered
        self.goal_group1.is_ordered = False
        same_goal_group.is_ordered = False

        # GoalGroups that are logically the same should return True
        # when compared via is_equal_to
        self.assertTrue(self.goal_group1.is_equal_to(same_goal_group))


if __name__ == '__main__':
    unittest.main()
