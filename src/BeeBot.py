"""This file defines the BeeBot class and the Heading Enum."""


from enum import Enum
from time import sleep
import pygame
from src.CustomEvent import CustomEvent


class Heading(Enum):
    """This class defines Enums for the heading of a BeeBot."""

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    FAIL = 5


class BeeBot(pygame.sprite.Sprite):
    """This class defines the BeeBot."""

    def __init__(self, scenario):
        """Create a BeeBot."""
        self.scenario = scenario  # Store so we can reset BeeBot

        # Initial position of the BeeBot in terms of square on the Board.
        start_logical_position = self.scenario.get_element('BeeBotStartPosition')
        start_logical_position_x = start_logical_position[0]  # x co-ord
        start_logical_position_y = start_logical_position[1]  # y co-ord

        # The amount the BeeBot moves.
        self.step = self.scenario.get_element('BoardStep')

        # The BeeBot's position of the BeeBot in terms of pixels.
        self.screen_location_x = start_logical_position_x * self.step
        self.screen_location_y = start_logical_position_y * self.step

        # The BeeBot's position of the BeeBot in terms of the Board.
        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

        # All the sprites the BeeBot may display.
        self.sprites = {}

        # Read the sprite and assign it as the "NORTH" sprite.
        base_sprite = self.scenario.get_element('BeeBotSprite')
        self.sprites[Heading.NORTH] = base_sprite

        # Define other sprites by rotating the "NORTH" sprite.
        self.sprites[Heading.EAST] = self.rotate(base_sprite, 270)
        self.sprites[Heading.SOUTH] = self.rotate(base_sprite, 180)
        self.sprites[Heading.WEST] = self.rotate(base_sprite, 90)
        self.sprites[Heading.FAIL] = self.scenario.get_element('BeeBotFailSprite')

        # Which way is the BeeBot facing.
        self.heading = self.scenario.get_element('BeeBotHeading')

        # Which sprite to display.
        self.sprite = self.sprites[self.heading]

        # Store MOVE_BEEBOT_* events here.
        self.memory = []

    def move(self, event):
        """Move the BeeBot."""
        if event.type == CustomEvent.MOVE_BEEBOT_UP:
            self.move_forward()
            sleep(0.5)  # wait to simulate BeeBot movement
        if event.type == CustomEvent.MOVE_BEEBOT_DOWN:
            self.move_backward()
            sleep(0.5)  # wait to simulate BeeBot movement
        if event.type == CustomEvent.MOVE_BEEBOT_LEFT:
            self.move_left()
            sleep(0.5)  # wait to simulate BeeBot movement
        if event.type == CustomEvent.MOVE_BEEBOT_RIGHT:
            self.move_right()
            sleep(0.5)  # wait to simulate BeeBot movement

    def add_to_memory(self, event):
        """Add "button press" to the BeeBot's "memory"."""
        self.memory.append(event)

    def push_out_memory(self):
        """Act out the instructions in the BeeBot's "memory"."""
        for instruction in self.memory:
            # we use pygame's event queue because we need to check
            # it regularly to prevent the game from crashing.
            pygame.event.post(instruction)

    def clear_memory(self):
        """Clear the BeeBot's "memory"."""
        self.memory = []

    def display(self, screen):
        """Display the BeeBot on screen."""
        screen.blit(self.sprite, (self.screen_location_x,
                                  self.screen_location_y))

    def move_backward(self):
        """Move the BeeBot backward."""
        # The origin is in the top left corner
        if self.heading == Heading.SOUTH:
            for _ in range(0, self.step):
                self.screen_location_y = self.screen_location_y - 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_y = self.logical_position_y - 1

        elif self.heading == Heading.WEST:
            for _ in range(0, self.step):
                self.screen_location_x = self.screen_location_x + 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_x = self.logical_position_x + 1

        elif self.heading == Heading.NORTH:
            for _ in range(0, self.step):
                self.screen_location_y = self.screen_location_y + 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_y = self.logical_position_y + 1

        elif self.heading == Heading.EAST:
            for _ in range(0, self.step):
                self.screen_location_x = self.screen_location_x - 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_x = self.logical_position_x - 1

    def move_forward(self):
        """Move the BeeBot forward."""
        # The origin is in the top left corner
        if self.heading == Heading.NORTH:
            for _ in range(0, self.step):
                self.screen_location_y = self.screen_location_y - 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_y = self.logical_position_y - 1

        elif self.heading == Heading.EAST:
            for _ in range(0, self.step):
                self.screen_location_x = self.screen_location_x + 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_x = self.logical_position_x + 1

        elif self.heading == Heading.SOUTH:
            for _ in range(0, self.step):
                self.screen_location_y = self.screen_location_y + 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_y = self.logical_position_y + 1

        elif self.heading == Heading.WEST:
            for _ in range(0, self.step):
                self.screen_location_x = self.screen_location_x - 1
                sleep(0.01)  # sleep prevents the BeeBot moving too quickly
            self.logical_position_x = self.logical_position_x - 1

    def move_right(self):
        """Turn the BeeBot right."""
        # No need to move the BeeBot, just change it's sprite.
        sleep(0.5)
        self.sprite = self.rotate(self.sprite, -45)
        sleep(0.5)

        if self.heading == Heading.NORTH:
            self.heading = Heading.EAST
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.EAST:
            self.heading = Heading.SOUTH
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.SOUTH:
            self.heading = Heading.WEST
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.WEST:
            self.heading = Heading.NORTH
            self.sprite = self.sprites[self.heading]

        sleep(0.5)

    def move_left(self):
        """Turn the BeeBot left."""
        # No need to move the BeeBot, just change it's sprite.
        sleep(0.5)
        self.sprite = self.rotate(self.sprite, 45)
        sleep(0.5)

        if self.heading == Heading.NORTH:
            self.heading = Heading.WEST
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.EAST:
            self.heading = Heading.NORTH
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.SOUTH:
            self.heading = Heading.EAST
            self.sprite = self.sprites[self.heading]

        elif self.heading == Heading.WEST:
            self.heading = Heading.SOUTH
            self.sprite = self.sprites[self.heading]

        sleep(0.5)

    def reset_position(self):
        # Initial position of the BeeBot in terms of square on the Board.
        start_logical_position = self.scenario.get_element('BeeBotStartPosition')
        start_logical_position_x = start_logical_position[0]  # x co-ord
        start_logical_position_y = start_logical_position[1]  # y co-ord

        self.heading = self.scenario.get_element('BeeBotHeading')

        # Which sprite to display.
        self.sprite = self.sprites[self.heading]

        # The BeeBot's position of the BeeBot in terms of pixels.
        self.screen_location_x = start_logical_position_x * self.step
        self.screen_location_y = start_logical_position_y * self.step

        # The BeeBot's position of the BeeBot in terms of the Board.
        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

    @classmethod
    def rotate(cls, image, angle):
        """Rotate given image by given angle."""
        image_copy = image.copy()  # this seems to stop thread errors
        orig_rect = image_copy.get_rect()
        rot_image = pygame.transform.rotate(image_copy, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        return rot_image.subsurface(rot_rect)
