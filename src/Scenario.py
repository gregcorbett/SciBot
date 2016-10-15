"""This file defines the Scenario class."""


from pickle import dump
import pygame
from src.GoalGroup import GoalGroup
from src.Goal import Goal
from src.ObstacleGroup import ObstacleGroup
from src.Obstacle import Obstacle
from src.Point import Point
from src import __version__


class Scenario():
    """This class defines the Scenario (theme) of the game."""

    def __init__(self, name):
        """Create empty Scenario called name."""
        # Will be popultaed with pickleable data
        self._elements = {}
        self._elements['Name'] = name
        self._elements['Version'] = __version__
        try:
            logo = pygame.image.load("./logo.png")
            logo_pickle = self.format_surface_for_pickle(logo)
            self._elements['Logo'] = logo_pickle
        except:
            self._elements['Logo'] = None

    def _get_element(self, key):
        """Safely access Scenario elements that may not exist."""
        if key not in self._elements:
            # If element isn't defined (possibly because the scenario is old)
            # this method will return None."""
            return None
        # Otherwise, return the stored element
        return self._elements[key]

    def get_logo(self):
        """Return the stored logo"""
        logo_pickle = self._get_element('Logo')
        logo = self.format_pickle_to_surface(logo_pickle)
        return logo

    def set_beebot_fail_sprite(self, sprite):
        """Store the fail sprite in pickle-able form."""
        sprite = pygame.image.load(sprite)
        pickled_sprite = self.format_surface_for_pickle(sprite)
        self._elements['BeeBotFailSprite'] = pickled_sprite

    def get_beebot_fail_sprite(self):
        """Return BeeBot fail sprte."""
        pickled_sprite = self._get_element('BeeBotFailSprite')
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

    def set_ordered_goals(self, ordered):
        """Set whether the Goals in the GoalGroup must be met in order."""
        self._elements['OrderedGoals'] = ordered

    def get_ordered_goals(self):
        """Return whether the Goals in the GoalGroup must be met in order."""
        return self._get_element('OrderedGoals')

    def get_goal_group(self):
        """Return the Scenario's GoalGroup."""
        # no guarantee OrderGoals is defined, so using get_element
        is_group_ordered = self._get_element('OrderedGoals')

        # Create a temp, empty, GoalGroup
        if is_group_ordered is None:
            goal_group = GoalGroup()  # use the class default
        elif is_group_ordered:
            goal_group = GoalGroup(True)
        else:
            goal_group = GoalGroup(False)

        # For each pickled goal, unpickle and add to the temp GoalGroup
        for pickled_goal in self._get_element('GoalGroup'):
            goal_sprite = self.format_pickle_to_surface(pickled_goal[0])
            goal = Goal(goal_sprite,
                        Point(pickled_goal[1], pickled_goal[2]),
                        self._get_element('BoardStep'))
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

    def get_obstacle_group(self):
        """Return the Scenario's ObstacleGroup."""
        # Create a temp, empty, ObstacleGroup
        obstacle_group = ObstacleGroup()

        # For each pickled Obstacle, unpickle and add to the temp ObstacleGroup
        for pickled_obs in self._get_element('ObstacleGroup'):
            obstacle_sprite = self.format_pickle_to_surface(pickled_obs[0])
            obstacle = Obstacle(obstacle_sprite,
                                Point(pickled_obs[1], pickled_obs[2]),
                                self._get_element('BoardStep'))

            # Add unpickled goal to temp GoalGroup
            obstacle_group.add(obstacle)
        # Return temp obstacle_group
        return obstacle_group

    def set_beebot_heading(self, heading):
        """Return the staring heading of the BeeBot."""
        self._elements['BeeBotHeading'] = heading

    def get_beebot_heading(self):
        """Set the staring heading of the BeeBot."""
        return self._get_element('BeeBotHeading')

    def set_beebot_sprite(self, image_file):
        """Set the "NORTH" BeeBot sprite."""
        sprite = pygame.image.load(image_file)
        self._elements['BeeBotSprite'] = self.format_surface_for_pickle(sprite)

    def get_beebot_sprite(self):
        """Return the "NORTH" BeeBot sprite."""
        return self.format_pickle_to_surface(self._get_element('BeeBotSprite'))

    def get_beebot_start_position(self):
        """Get the BeeBot's starting position."""
        return self._get_element('BeeBotStartPosition')

    def set_beebot_start_position(self, x_coord, y_coord):
        """Set the BeeBot's starting position."""
        self._elements['BeeBotStartPosition'] = (x_coord, y_coord)

    def get_logical_height(self):
        """Get the Board height."""
        return self._get_element('LogicalHeight')

    def get_logical_width(self):
        """Get the Board width."""
        return self._get_element('LogicalWidth')

    def set_logical_height(self, height):
        """Set the Board height."""
        self._elements['LogicalHeight'] = height

    def set_logical_width(self, width):
        """Set the Board width."""
        self._elements['LogicalWidth'] = width

    def get_board_step(self):
        """Return the Board step (aka how far the BeeBot moves.)."""
        return self._get_element('BoardStep')

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

    def get_background(self):
        """Return the Background of this Scenario."""
        return self.format_pickle_to_surface(self._elements['Background'])

    def set_border_colour(self, colour):
        """Set the Border Colour of this Scenario."""
        self._elements['BorderColour'] = colour

    def get_border_colour(self):
        """Return the Border Colour of this Scenario."""
        return self._get_element('BorderColour')

    def get_name(self):
        """Return the Name of this Scenario."""
        return self._get_element('Name')

    def get_version(self):
        """Return the Version of this Scenario."""
        return self._get_element('Version')

    def write_to_file(self):
        """Dump the contents of this Scenario to a scibot file."""
        dump(self,
             open("./scenarios/" + self._elements['Name'] + ".scibot",
                  "wb"))
