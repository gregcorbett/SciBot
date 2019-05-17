"""This file defines the Scenario class."""


from pickle import dump
import pygame
from src.Component import Component
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
        except pygame.error:
            self._elements['Logo'] = None

    def _get_element(self, key):
        """Safely access Scenario elements that may not exist."""
        if key not in self._elements:
            # If element isn't defined (possibly because the scenario is old)
            # this method will return None."""
            return None
        # Otherwise, return the stored element
        return self._elements[key]

    def set_license(self, text):
        """Set the LICENSE of this Scenario."""
        self._elements['License'] = text

    def get_license(self):
        """Get the LICENSE of this Scenario."""
        return self._get_element('License')

    def get_logo(self):
        """Return the stored logo."""
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

    def add_goal(self, x_coord, y_coord, sprite=None, should_increment_beebot_sprite=False):
        """Add a goal to this Scenario."""
        # if no GoalGroup, create an empty one.
        if 'GoalGroup' not in self._elements:
            self._elements['GoalGroup'] = []

        # Handle the different use cases for saving Component sprites.
        sprite_list = self.listify(sprite)
        # Prepare sprite(s) (if any) for pickling.
        sprite_list = self.format_surface_list_for_pickle(sprite_list)
        # Store Goal in pickle-able format
        self._elements['GoalGroup'].append(
            (sprite_list, x_coord, y_coord, should_increment_beebot_sprite)
        )

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
            sprite_list = pickled_goal[0]
            position = Point(pickled_goal[1], pickled_goal[2])
            # Only v1.2+ Scerarios provide the should_increment_beebot_sprite
            # variable, so handle the cases when it's not provided.
            try:
                should_increment_beebot_sprite = pickled_goal[3]
            except IndexError:
                should_increment_beebot_sprite = False

            # Handle the different use cases for reading Component sprites.
            sprite_list = self.listify(sprite_list)

            # Un-pickle the sprite list.
            sprite_list = self.format_pickle_list_to_surface(sprite_list)

            # Create an un-pickled Goal from the pickled data.
            goal = Goal(
                sprite_list, position, self._get_element('BoardStep'),
                should_increment_beebot_sprite,
            )
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
            # Because the Obstacle class extends the Component class, we have
            # to use a list in the constructor, even though multi sprite
            # Obstacles aren't a thing.
            obstacle = Obstacle([obstacle_sprite],
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
        """Set the "NORTH" BeeBot sprites."""
        # Handle the different use cases for saving Component sprites.
        image_list = self.listify(image_file)
        # Prepare sprite(s) (if any) for pickling.
        pickleable_list = self.format_surface_list_for_pickle(image_list)
        # Add the pickleable list to the Scenario.
        self._elements['BeeBotSprite'] = pickleable_list

    def get_beebot_sprite(self):
        """Get the "NORTH" BeeBot sprites."""
        sprite_list = self._get_element('BeeBotSprite')
        # Handle the different use cases for reading Component sprites.
        sprite_list = self.listify(sprite_list)
        # Un-pickle the sprites.
        sprite_list = self.format_pickle_list_to_surface(sprite_list)

        return sprite_list

    def get_beebot_start_position(self):
        """Get the BeeBot's starting position."""
        return self._get_element('BeeBotStartPosition')

    def set_beebot_start_position(self, x_coord, y_coord):
        """Set the BeeBot's starting position."""
        self._elements['BeeBotStartPosition'] = Point(x_coord, y_coord)

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
    def listify(cls, sprite):
        """
        Handle the different use cases for saving or reading component sprites.

        If the argument is a list, this method will return the arguement.
        Otherwise, this method returns a list containing only the argument.
        """
        # Case: A list of sprite objects, pickleable surfaces or images.
        if isinstance(sprite, list):
            return sprite
        # Case: A sprite object, pickleable surface, image or None.
        return [sprite]

    @classmethod
    def format_pickle_to_surface(cls, pickled_image):
        """Return an image from a pickle-able format."""
        if pickled_image is None:
            return None
        return pygame.image.fromstring(pickled_image['image'],
                                       pickled_image['size'],
                                       pickled_image['format'])

    @classmethod
    def format_pickle_list_to_surface(cls, pickled_list):
        # Un-pickle the sprite.
        for index, sprite in enumerate(pickled_list):
            pickled_list[index] = cls.format_pickle_to_surface(sprite)

        return pickled_list

    @classmethod
    def format_surface_for_pickle(cls, image):
        """Return an pickle-able format from an image."""
        if image is None:
            return None
        return {'image': pygame.image.tostring(image, "RGBA"),
                'size': image.get_size(),
                'format': "RGBA"}

    @classmethod
    def format_surface_list_for_pickle(cls, sprite_list):
        # Prepare sprite(s) (if any) for pickling.
        for index, file_path in enumerate(sprite_list):
            # If file_path is None, store None in sprite_list.
            if file_path is None:
                sprite_list[index] = None
            # Else try to load and prepare an image.
            else:
                surface = pygame.image.load(file_path)
                pickleable_surface = cls.format_surface_for_pickle(surface)
                sprite_list[index] = pickleable_surface

        return sprite_list

    def set_background(self, background_image):
        """Set the Background of this Scenario."""
        background = pygame.image.load(background_image)
        pickled_background = self.format_surface_for_pickle(background)
        self._elements['Background'] = pickled_background

    def get_background(self):
        """
        Return a list containing only the Background of this Scenario.

        This method returns a list containing only the Background because
        the Board class extends the Component class
        which expects a list of images.
        """
        return [self.format_pickle_to_surface(self._elements['Background'])]

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
