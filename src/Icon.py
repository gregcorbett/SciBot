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

        self.vertices = []

        if text == 'Forward':
            self.vertices = Arrow.FORWARD.value
        elif text == 'Turn Left':
            self.vertices = Arrow.LEFT.value
        elif text == 'Turn Right':
            self.vertices = Arrow.RIGHT.value
        elif text == 'Backward':
            self.vertices = Arrow.BACKWARD.value

        if self.vertices:
            self.vertices = self._get_vertex_list(self.vertices,
                                                  self.rect.centerx,
                                                  self.rect.centery)

    def _get_vertex_list(self, array, center_x, center_y):
        """Return usable list of vertices for pygame.draw.polygon."""
        to_return = []
        # For each vector
        for i in range(0, len(array)):
            current = array[i]
            # Append a vertex tuple to to_return
            to_return.append(
                (
                    current[0] + center_x,
                    current[1] + center_y
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
