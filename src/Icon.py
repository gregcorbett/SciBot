"""
This file defines the Icon class.

Extend this class to create Game Window Icons like the Buttons.

The file also contains classes to help create symbols on those Icons.
"""
from enum import Enum
import pygame


class Icon():
    """This class defines an individual Icon."""

    def __init__(self,
                 text,  # The text to display (can be None)
                 text_colour,  # The colour of the text/polygons (can be None)
                 background_colour,  # The colour of the text (can be None)
                 screen_location,  # The position on the screen
                 size,  # The size of the Icon
                 displayed=True):  # Display Icon if True
        """Create an Icon."""
        self.text = text
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.screen_location = screen_location
        self.size = size
        self.rect = pygame.Rect(screen_location, size)
        self.font = pygame.font.SysFont("comicsansms", 22)
        self.displayed = displayed

        self.vertices = self._text_to_shape(self.text)

        if self.vertices:
            self.vertices = self._get_vertex_list(self.vertices,
                                                  self.rect.center,
                                                  self.size)

    @classmethod
    def _text_to_shape(cls, text):
        """Return an Icon shape based on the provided text."""
        # A dictionary mapping text to Icon shapes
        shape_dict = {
            "Forward": Arrow.FORWARD.value,
            "Turn Left": Arrow.LEFT.value,
            "Turn Right": Arrow.RIGHT.value,
            "Backward": Arrow.BACKWARD.value,
        }

        try:
            return shape_dict[text]
        except KeyError:
            # If the text is not in the shape_dict, return an empty list as
            # the text doesn't correspond to any Icon shape.
            return []

    def _get_vertex_list(self, array, center, size=(120, 120)):
        """Return a translated list of vertices within the given size."""
        to_return = []
        # For each vector
        for i in range(0, len(array)):
            current = array[i]
            # Append a vertex tuple to to_return
            to_return.append(
                (
                    # We assume all Icon shapes are originally 120x120
                    (current[0] * size[0] / 120) + center[0],
                    (current[1] * size[1] / 120) + center[1]
                )
            )
        return to_return

    def display(self, screen):
        """Draw the Icon object on screen, if self.displayed is True."""
        if self.displayed:
            # Draw the Icon background
            screen.fill(self.background_colour, rect=self.rect)

            # If list of vectors is empty
            if self.vertices == []:
                # Draw the Icon text
                text = self.font.render(self.text,
                                        True,
                                        self.text_colour)

                # Center the background and text
                text_rect = text.get_rect()
                text_rect.centerx = self.rect.centerx
                text_rect.centery = self.rect.centery

                # Render Icon on screen
                screen.blit(text, text_rect)

            else:
                pygame.draw.polygon(screen, self.text_colour, self.vertices)


class Arrow(Enum):
    """This class defines Enums for the arrow polygon of a Icon."""

    # Array of vectors for each arrow
    FORWARD = [(20, -20), (0, -40), (-20, -20), (-10, -20), (-10, 40),
               (10, 40), (10, -20)]

    LEFT = [(-20, -40), (-40, -20), (-20, 0), (-20, -10), (10, -10),
            (10, 20), (-30, 20), (-30, 40), (30, 40), (30, -30),
            (-20, -30)]

    RIGHT = [(20, -40), (40, -20), (20, 0), (20, -10), (-10, -10),
             (-10, 20), (30, 20), (30, 40), (-30, 40), (-30, -30),
             (20, -30)]

    BACKWARD = [(20, 20), (0, 40), (-20, 20), (-10, 20), (-10, -40),
                (10, -40), (10, 20)]
