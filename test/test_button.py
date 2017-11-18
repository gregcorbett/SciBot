"""This file contains the TestButton class."""

import unittest
import pygame
from src.Button import Button
from src.GameWindow import GameWindow


class TestButton(unittest.TestCase):
    """This test class unit tests the Button class."""

    def setUp(self):
        """Create two test Buttons and start pygame."""
        pygame.init()

        # Create a test Button with text
        self.test_text_button = Button('text', GameWindow.BLACK,
                                       GameWindow.WHITE, (0, 0), (10, 10))

        # Create a test Button with an Arrow
        self.test_icon_button = Button('Forward', GameWindow.BLACK,
                                       GameWindow.WHITE, (0, 0), (10, 10))

    @classmethod
    def test_init(cls):
        """Test the init method of the Button class."""
        button_text = ['Forward', 'Turn Left', 'Turn Right',
                       'Backward', 'Other']

        for text in button_text:
            # Attempt to create a Button, if any fail the test will fail
            _unused_button = Button(text,
                                    GameWindow.BLACK, GameWindow.WHITE,
                                    (0, 0), (10, 10))

    def test_get_vertex_list(self):
        """Test the _get_vertex_list method."""
        input_list = [(0, 0), (5, 0), (0, -5)]
        center_x = 10
        center_y = 10

        # _get_vertex_list(input_list, center_x, center_y) should map
        # (0,0) of the input_list to center_x and center_y (and all other
        # points accordingly)
        expected_output = [(10, 10), (15, 10), (10, 5)]

        # We need to use an instance of the Button class
        # to call the _get_vertex_list method
        output = self.test_text_button._get_vertex_list(input_list,
                                                        center_x,
                                                        center_y)

        self.assertEqual(expected_output, output)

    def test_display(self):
        """
        Test the display method of a Button.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test Buttons
        self.test_text_button.display(test_screen)
        self.test_icon_button.display(test_screen)

        # Make this Button not displayed
        self.test_icon_button.displayed = False
        # This will test the branch of code for when you attempt to
        # display a non displayed Button
        self.test_icon_button.display(test_screen)
        # We don't have to worry about re-displaying the Button
        # as each test case recreates the test buttons

    def test_swap_colours(self):
        """Test the swap_colours method."""
        # Store the original colours of the Buttons text and background
        text_colour = self.test_text_button.text_colour
        background_colour = self.test_text_button.background_colour

        # Swap the colours
        self.test_text_button.swap_colours()

        # Assert the colour of the text is now background_colour
        self.assertEqual(self.test_text_button.text_colour,
                         background_colour)

        # Assert the colour of the background is now the text colour
        self.assertEqual(self.test_text_button.background_colour,
                         text_colour)

        # Assert the Button has registered it has been swapped
        self.assertTrue(self.test_text_button.swapped)

        # We don't have to worry about un-swapping the Button
        # as each test case recreates the test buttons

    def test_is_mouse_over_button(self):
        """Test the is_mouse_over_button."""
        # Assert that a mouse position outside the Button does not return True
        self.assertFalse(self.test_text_button.is_mouse_over_button((5, -2)))
        self.assertFalse(self.test_text_button.is_mouse_over_button((-2, 5)))
        self.assertFalse(self.test_text_button.is_mouse_over_button((12, 5)))
        self.assertFalse(self.test_text_button.is_mouse_over_button((5, 12)))

        # Assert that a mouse position inside the Button does return True
        self.assertTrue(self.test_text_button.is_mouse_over_button((5, 5)))

        # Make this Button not displayed
        self.test_icon_button.displayed = False
        # Assert that a mouse position inside a non displayed Button
        # does not return True
        self.assertFalse(self.test_icon_button.is_mouse_over_button((5, 5)))
        # We don't have to worry about re-displaying the Button
        # as each test case recreates the test buttons


if __name__ == "__main__":
    unittest.main()
