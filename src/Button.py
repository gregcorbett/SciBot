"""This file defines the Button class."""
from enum import Enum
from src.Icon import Icon


class Arrow(Enum):
    """This class defines Enums for the arrow polygon of a button."""

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


class Button(Icon):
    """This class defines an individual Button."""

    def __init__(self,
                 text,  # The text to display (can be None)
                 text_colour,  # The colour of the text/polygons (can be None)
                 background_colour,  # The colour of the text (can be None)
                 screen_location,  # The position on the screen
                 size,  # The size of the Button
                 displayed=True):  # Display Button if True
        """Create a Button."""
        super().__init__(text,
                         text_colour, background_colour,
                         screen_location, size,
                         displayed)

        self.swapped = False  # Keeps track of wether a Button is swapped

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

    def swap_colours(self):
        """Swap the background and text / polygon colour of the Button."""
        temp_colour = self.text_colour
        self.text_colour = self.background_colour
        self.background_colour = temp_colour
        self.swapped = not self.swapped

    def is_mouse_over_button(self, mouse_position):
        """Given a mouse position, return True if mouse over Button."""
        return (mouse_position[0] > self.rect.topleft[0] and
                mouse_position[1] > self.rect.topleft[1] and
                mouse_position[0] < self.rect.bottomright[0] and
                mouse_position[1] < self.rect.bottomright[1] and
                # Can't click on a Button that isn't displayed
                self.displayed)
