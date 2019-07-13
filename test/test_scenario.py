"""This file contains the TestScenario class."""
import os
import pickle
import pygame
import unittest

from src.BeeBot import Heading
from src.Goal import Goal
from src.GoalGroup import GoalGroup
from src.Obstacle import Obstacle
from src.ObstacleGroup import ObstacleGroup
from src.Point import Point
from src.Scenario import Scenario


class TestScenario(unittest.TestCase):
    """This test class unit tests the Scenario class."""

    def setUp(self):
        scenario = Scenario('Test')
        scenario.set_board_step(150)
        scenario.set_logical_width(5)
        scenario.set_logical_height(8)
        scenario.set_beebot_start_position(3, 1)
        scenario.set_beebot_sprite('./img/Default/robot.jpg')
        scenario.set_beebot_heading(Heading.NORTH)
        scenario.set_background('./img/Default/background.jpg')
        scenario.set_border_colour((0, 0, 0))
        scenario.add_obstacle(2, 1)
        scenario.add_obstacle(2, 3)
        scenario.add_goal(1, 2)
        scenario.add_goal(2, 0)
        scenario.set_ordered_goals(False)
        scenario.set_beebot_fail_sprite('./img/Default/robotx.jpg')
        scenario.set_license('Test License')

        # Writes the scibot file
        scenario.write_to_file()

    def tearDown(self):
        os.remove('scenarios/Test.scibot')

    def test_loaded_scenario(self):
        with open('scenarios/Test.scibot', 'rb') as test_scenario:
            loaded_scenario = pickle.load(test_scenario)

        # Assert all the values are as we would expect
        self.assertEqual(loaded_scenario.get_board_step(), 150)
        self.assertEqual(loaded_scenario.get_logical_width(), 5)
        self.assertEqual(loaded_scenario.get_logical_height(), 8)
        self.assertEqual(loaded_scenario.get_beebot_start_position(), (3, 1))

        # To compare the loaded Sprite with the Sprite from the scenario,
        # we have to access _elements directly here we cant compare surfaces
        # for equality and the get method would turn the saved
        # picklable image as a surface
        saved_sprite_surface_list = loaded_scenario._elements['BeeBotSprite']
        self._compare_image_to_pickle('img/Default/robot.jpg',
                                      saved_sprite_surface_list[0])

        self.assertEqual(loaded_scenario.get_beebot_heading(), Heading.NORTH)

        saved_sprite_surface = loaded_scenario._elements['Background']
        self._compare_image_to_pickle('img/Default/background.jpg',
                                      saved_sprite_surface)

        self.assertEqual(loaded_scenario.get_border_colour(), (0, 0, 0))

        # To compare ObstacleGroups we must craft one first
        obstacle_group = ObstacleGroup()
        obstacle_1 = Obstacle([None], Point(2, 1), 150)
        obstacle_2 = Obstacle([None], Point(2, 3), 150)
        obstacle_group.add(obstacle_1)
        obstacle_group.add(obstacle_2)
        self.assertTrue(loaded_scenario.get_obstacle_group().is_equal_to(obstacle_group))

        # To compare GoalGroups we must craft one first
        goal_group = GoalGroup()
        goal_1 = Goal([None], Point(1, 2), 150)
        goal_2 = Goal([None], Point(2, 0), 150)
        goal_group.add(goal_1)
        goal_group.add(goal_2)
        goal_group.is_ordered = False
        # Not sure how to test this yet
        self.assertTrue(loaded_scenario.get_goal_group().is_equal_to(goal_group))

        self.assertEqual(loaded_scenario.get_ordered_goals(), False)

        saved_sprite_surface = loaded_scenario._elements['BeeBotFailSprite']
        self._compare_image_to_pickle('img/Default/robotx.jpg',
                                      saved_sprite_surface)

        self.assertEqual(loaded_scenario.get_license(), 'Test License')

    def _compare_image_to_pickle(self, image, saved_picklable_image):
        """
        Compare the image to the saved_picklable_image.

        To do this, the image is loaded and prepared for pickling before
        being compared to the saved_picklable_image.

        We cant compare surfaces for equality directly so we have to use
        the  picklable representation.
        """
        # Load the image
        surface = pygame.image.load(image)
        # Prepare the image for pickling
        picklable_surface = Scenario.format_surface_for_pickle(surface)
        # Compare the picklable given image with the saved picklable image
        self.assertEqual(picklable_surface, saved_picklable_image)

if __name__ == '__main__':
    unittest.main()
