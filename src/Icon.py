"""
This file defines the Icon class.

Extend this class to create Game Window Icons like the Buttons.
"""
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
