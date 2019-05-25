"""This class contains the TestIcon class."""
import unittest
import pygame
from src.GameWindow import GameWindow
from src.Icon import Icon
from src.Point import Point


class TestIcon(unittest.TestCase):
    """This class unit tests the Icon class."""

    def setUp(self):
        """Create a Test Icon and start pygame."""
        pygame.init()
        self.test_text_icon = Icon('test icon',
                                   GameWindow.BLACK, GameWindow.WHITE,
                                   Point(0, 0), (10, 10))

        self.test_vertex_icon = Icon('vertex icon',
                                     GameWindow.BLACK, GameWindow.WHITE,
                                     Point(0, 0), (10, 10))

        self.test_vertex_icon.vertices = [(10, 10), (-10, -10), (0, 0)]

    @classmethod
    def test_init(cls):
        """Test the init method of the Icon class."""
        _unused_icon = Icon('test icon',
                            GameWindow.BLACK, GameWindow.WHITE,
                            Point(0, 0), (10, 10))

    def test_get_vertex_list(self):
        """Test the _get_vertex_list method."""
        input_list = [Point(0, 0), Point(5, 0), Point(0, -5)]
        center = (10, 10)

        # _get_vertex_list(input_list, center_x, center_y) should map
        # (0,0) of the input_list to center_x and center_y (and all other
        # points accordingly)
        expected_output = [Point(10, 10), Point(15, 10), Point(10, 5)]

        # We need to use an instance of the Icon class
        # to call the _get_vertex_list method
        output = self.test_text_icon._get_vertex_list(input_list, center)

        self.assertEqual(expected_output, output)

    def test_display(self):
        """
        Test the display method of a Icon.

        All this really does is make sure the method executes correctly.
        If the method call errors, the test will fail.
        """
        # Create a test screen to dsiplay things on
        test_screen = pygame.display.set_mode((1500, 1500))

        # Attempt to display the test text Icon
        self.test_text_icon.display(test_screen)

        # Attempt to display the test vertex Icon
        self.test_vertex_icon.display(test_screen)

        # Make the test text Icon not displayed
        self.test_text_icon.displayed = False
        # This will test the branch of code for when you attempt to
        # display a non displayed Icon
        self.test_text_icon.display(test_screen)
        # We don't have to worry about re-displaying the Icon
        # as each test case recreates the test Icon


if __name__ == "__main__":
    unittest.main()
