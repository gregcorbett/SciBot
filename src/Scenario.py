"""This file defines the Scenario class."""


from pickle import dump
import pygame
from src.GoalGroup import GoalGroup
from src.Goal import Goal
from src.ObstacleGroup import ObstacleGroup
from src.Obstacle import Obstacle


class Scenario():
    """This class defines the Scenario (theme) of the game."""

    def __init__(self, name):
        """Create empty Scenario called name."""
        self._elements = {}
        self._elements['Name'] = name

    def get_element(self, key):
        """Safely access Scenario elements."""
        if key not in self._elements:
            # if element isn't defined (possibly because the scenario is old)
            # this method will return None."""
            return None

        # Defines keys and _get methods
        # This essentially performs a run time check that any defined key has
        # a defined _get method.
        switcher = {
            'Name': self._get_name(),
            'BoardStep': self._get_board_step(),
            'LogicalWidth': self._get_logical_width(),
            'LogicalHeight': self._get_logical_height(),
            'Background': self._get_background(),
            'BorderColour': self._get_border_colour(),
            'BeeBotSprite': self._get_beebot_sprite(),
            'BeeBotStartPosition': self._get_beebot_start_position(),
            'BeeBotHeading': self._get_beebot_heading(),
            'ObstacleGroup': self._get_obstacle_group(),
            'GoalGroup': self._get_goal_group(),
            'BeeBotFailSprite': self._get_beebot_fail_sprite(),
        }

        return switcher.get(key)

    def set_beebot_fail_sprite(self, sprite):
        """Store the fail sprite in pickle-able form."""
        sprite = pygame.image.load(sprite)
        pickled_sprite = self.format_surface_for_pickle(sprite)
        self._elements['BeeBotFailSprite'] = pickled_sprite

    def _get_beebot_fail_sprite(self):
        """Return BeeBot fail sprte."""
        pickled_sprite = self._elements['BeeBotFailSprite']
        return self.format_pickle_to_surface(pickled_sprite)

    def add_goal(self, x_coord, y_coord, sprite=None):
        """Add a goal to this Scenario."""
        # if no GoalGroup, create an empty one.
        if 'GoalGroup' not in self._elements:
            self._elements['GoalGroup'] = []

        # prepare sprite (if any) for pickling
        if sprite is not None:
            sprite = pygame.image.load(sprite)
            sprite = self.format_surface_for_pickle(sprite)

        # Store Goal in pickle-able format
        self._elements['GoalGroup'].append((sprite, x_coord, y_coord))

    def _get_goal_group(self):
        """Return the Scenario's GoalGroup."""
        # Create a temp, empty, GoalGroup
        goal_group = GoalGroup()

        # For each pickled goal, unpickle and add to the temp GoalGroup
        for pickled_goal in self._elements['GoalGroup']:
            goal_sprite = self.format_pickle_to_surface(pickled_goal[0])
            goal = Goal(goal_sprite,
                        pickled_goal[1],
                        pickled_goal[2],
                        self._elements['BoardStep'])
            # Add unpickled goal to temp GoalGroup
            goal_group.add(goal)
        # Return temp GoalGroup
        return goal_group

    def add_obstacle(self, x_coord, y_coord, sprite=None):
        """Add an Obstacle to this Scenario."""
        # if no ObstacleGroup, create one
        if 'ObstacleGroup' not in self._elements:
            self._elements['ObstacleGroup'] = []

        # prepare sprite (if any) for pickling
        if sprite is not None:
            sprite = pygame.image.load(sprite)
            sprite = self.format_surface_for_pickle(sprite)

        # Store Obstacle in pickle-able form
        self._elements['ObstacleGroup'].append((sprite, x_coord, y_coord))

    def _get_obstacle_group(self):
        """Return the Scenario's ObstacleGroup."""
        # Create a temp, empty, ObstacleGroup
        obstacle_group = ObstacleGroup()

        # For each pickled Obstacle, unpickle and add to the temp ObstacleGroup
        for pickled_obs in self._elements['ObstacleGroup']:
            obstacle_sprite = self.format_pickle_to_surface(pickled_obs[0])
            obstacle = Obstacle(obstacle_sprite,
                                pickled_obs[1],
                                pickled_obs[2],
                                self._elements['BoardStep'])

            # Add unpickled goal to temp GoalGroup
            obstacle_group.add(obstacle)
        # Return temp obstacle_group
        return obstacle_group

    def set_beebot_heading(self, heading):
        """Return the staring heading of the BeeBot."""
        self._elements['BeeBotHeading'] = heading

    def _get_beebot_heading(self):
        """Set the staring heading of the BeeBot."""
        return self._elements['BeeBotHeading']

    def set_beebot_sprite(self, image_file):
        """Set the "NORTH" BeeBot sprite."""
        sprite = pygame.image.load(image_file)
        self._elements['BeeBotSprite'] = self.format_surface_for_pickle(sprite)

    def _get_beebot_sprite(self):
        """Return the "NORTH" BeeBot sprite."""
        return self.format_pickle_to_surface(self._elements['BeeBotSprite'])

    def _get_beebot_start_position(self):
        """Get the BeeBot's starting position."""
        return self._elements['BeeBotStartPosition']

    def set_beebot_start_position(self, x_coord, y_coord):
        """Set the BeeBot's starting position."""
        self._elements['BeeBotStartPosition'] = (x_coord, y_coord)

    def _get_logical_height(self):
        """Get the Board height."""
        return self._elements['LogicalHeight']

    def _get_logical_width(self):
        """Get the Board width."""
        return self._elements['LogicalWidth']

    def set_logical_height(self, height):
        """Set the Board height."""
        self._elements['LogicalHeight'] = height

    def set_logical_width(self, width):
        """Set the Board width."""
        self._elements['LogicalWidth'] = width

    def _get_board_step(self):
        """Return the Board step (aka how far the BeeBot moves.)."""
        return self._elements['BoardStep']

    def set_board_step(self, step):
        """Set the Board step (aka how far the BeeBot moves.)."""
        self._elements['BoardStep'] = step

    @classmethod
    def format_pickle_to_surface(cls, pickled_image):
        """Return an image from a pickle-able format."""
        if pickled_image is None:
            return None
        return pygame.image.fromstring(pickled_image['image'],
                                       pickled_image['size'],
                                       pickled_image['format'])

    @classmethod
    def format_surface_for_pickle(cls, image):
        """Return an pickle-able format from an image."""
        if image is None:
            return None
        return {'image': pygame.image.tostring(image, "RGBA"),
                'size': image.get_size(),
                'format': "RGBA"}

    def set_background(self, background_image):
        """Set the Background of this Scenario."""
        background = pygame.image.load(background_image)
        pickled_background = self.format_surface_for_pickle(background)
        self._elements['Background'] = pickled_background

    def _get_background(self):
        """Return the Background of this Scenario."""
        return self.format_pickle_to_surface(self._elements['Background'])

    def set_border_colour(self, colour):
        """Set the Border Colour of this Scenario."""
        self._elements['BorderColour'] = colour

    def _get_border_colour(self):
        """Return the Border Colour of this Scenario."""
        return self._elements['BorderColour']

    def _get_name(self):
        """Return the Name of this Scenario."""
        return self._elements['Name']

    def write_to_file(self):
        """Dump the contents of this Scenario to a scibot file."""
        dump(self,
             open("./scenarios/" + self._elements['Name'] + ".scibot",
                  "wb"))
