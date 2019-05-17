"""This file contains the TestComponent class."""
import unittest
import pygame

from src.Component import Component
from src.Point import Point


class TestComponent(unittest.TestCase):
    """This test class unit tests the Component class."""

    def setUp(self):
        """Create a simple Component for testing."""
        self.test_component = Component(["A", "B"], Point(0, 0), 0)

    def test_increment_sprite(self):
        """Test that the increment_sprite method behaves as expected."""
        # Confirm the current value of the Component's sprite.
        self.assertEqual(self.test_component.sprite, "A")

        # Call the Component's increment_sprite method.
        self.test_component.increment_sprite()

        # Confirm the new value of the Component's sprite.
        self.assertEqual(self.test_component.sprite, "B")

        # Confirm that calling the Component's increment_sprite method does
        # not effect the sprite.
        self.test_component.increment_sprite()
        self.assertEqual(self.test_component.sprite, "B")

    @classmethod
    def test_init(cls):
        """Test the init method of the Component class."""
        _unused_component = Component([None], Point(0, 0), 0)

    @classmethod
    def test_display(cls):
        """
        Test the display method of a Component.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test sprite list
        sprite_list = [pygame.image.load('img/Default/obstacle1.jpg')]

        # Create two test Component, one with a sprite and one without
        component_with_sprite = Component(sprite_list, Point(1, 1), 150)
        component_without_sprite = Component([None], Point(1, 1), 150)

        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the Component with a sprite
        component_with_sprite.display(test_screen)

        # Attempt to display the Component without a sprite
        component_without_sprite.display(test_screen)

    def test_is_equal_to(self):
        """Test the is_equal_to_method."""
        # Create a test sprite list.
        obstacle_sprite_list = [pygame.image.load('img/Default/obstacle1.jpg')]
        goal_sprite_list = [pygame.image.load('img/Default/goal1.jpg')]

        component = Component(obstacle_sprite_list, Point(1, 1), 150)
        # Create a Component equal to component
        component_copy = Component(obstacle_sprite_list, Point(1, 1), 150)
        # Create a Component in a different logical place
        component_diff_logical_pos = Component(obstacle_sprite_list,
                                               Point(2, 2), 150)
        # Create a Component with a different sprite
        component_diff_sprite = Component(goal_sprite_list, Point(1, 1), 150)

        # Check that equal Components are infact eqaul
        self.assertTrue(component.is_equal_to(component_copy))
        # Check that a Components in a different logical place is not equal
        self.assertFalse(component.is_equal_to(component_diff_logical_pos))
        # Check an Component with a different Sprite is not equal
        self.assertFalse(component.is_equal_to(component_diff_sprite))


if __name__ == '__main__':
    unittest.main()
