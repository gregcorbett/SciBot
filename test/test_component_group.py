"""This file contains the TestComponentGroup class."""
import unittest
import pygame

from src.Component import Component
from src.ComponentGroup import ComponentGroup
from src.Point import Point


class TestComponentGroup(unittest.TestCase):
    """This test class unit tests the ComponentGroup class."""

    def setUp(self):
        """Create ComponentGroups and Components used in testing."""
        # Create Components.
        self.component1 = Component(None, Point(1, 1), 150)
        self.component2 = Component(None, Point(2, 2), 150)
        self.component3 = Component(None, Point(3, 3), 150)

        # Create a ComponentGroup.
        self.component_group1 = ComponentGroup()
        self.component_group1.add(self.component1)
        self.component_group1.add(self.component2)

    def test_add(self):
        """Test the add method in isolation."""
        # Create an empty ComponentGroup for this test.
        new_component_group = ComponentGroup()

        # Add some Components to it.
        new_component_group.add(self.component1)
        new_component_group.add(self.component2)

        # Assert we have added 2 Components.
        self.assertEqual(len(new_component_group.components), 2)
        # Assert they are the right Components.
        self.assertTrue(
            new_component_group.components[0].is_equal_to(self.component1)
        )
        self.assertTrue(
            new_component_group.components[1].is_equal_to(self.component2)
        )

    def test_display(self):
        """
        Test the display method of a ComponentGroup.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on.
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test ComponentGroup.
        self.component_group1.display(test_screen)

    def test_is_equal_to(self):
        """Test is_equal_to()."""
        # Create a new ComponentGroup logically equal to self.component1
        equal_component_group = ComponentGroup()
        equal_component_group.add(self.component1)
        equal_component_group.add(self.component2)

        # Assert the new ComponentGroup is in fact equal.
        self.assertTrue(self.component_group1.is_equal_to(
            equal_component_group))

        # Create a 'differently ordered' ComponentGroup.
        component_group2 = ComponentGroup()
        component_group2.add(self.component2)
        component_group2.add(self.component1)

        # Assert the 'differently ordered' ComponentGroups are equal.
        self.assertTrue(self.component_group1.is_equal_to(component_group2))

        # Create a unequal ComponentGroup
        unequal_component_group = ComponentGroup()
        unequal_component_group.add(self.component2)
        unequal_component_group.add(self.component3)

        # Assert the unequal ComponentGroup are indeed unequal.
        self.assertFalse(self.component_group1.is_equal_to(
            unequal_component_group),
                         "Unequal ComponentGroups are equal.")

    def test_is_equal_to_uneq_larger(self):
        """Test two differently sized ComponentGroups for equality."""
        # Create a larger ComponentGroup
        larger_component_group = ComponentGroup()
        larger_component_group.add(self.component1)
        larger_component_group.add(self.component2)
        larger_component_group.add(self.component3)

        self.assertFalse(self.component_group1.is_equal_to(
            larger_component_group),
                         "Different sized ComponentGroups are equal.")

    def test_is_equal_to_same_component(self):
        """
        Test logically equal ComponentGroups for equality.

        This particular test case catches when the underlying objects
        are different but the ComponentGroups are the same.
        """
        # same_component1 is a different python object to self.component1,
        # but logically are the same. The same is true for same_component2.
        same_component1 = Component(None, Point(1, 1), 150)
        same_component2 = Component(None, Point(2, 2), 150)

        # same_component_group is a different python object
        # to self.component_group1, but logically are the same.
        same_component_group = ComponentGroup()
        same_component_group.add(same_component1)
        same_component_group.add(same_component2)

        # Set both ComponentGroups to be un ordered
        self.component_group1.is_ordered = False
        same_component_group.is_ordered = False

        # ComponentGroups that are logically the same should return True
        # when compared via is_equal_to
        self.assertTrue(self.component_group1.is_equal_to(
            same_component_group))


if __name__ == '__main__':
    unittest.main()
