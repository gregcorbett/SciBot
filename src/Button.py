"""This file defines the Button class."""
import pygame


class Button:
    """This class defines an individual Button."""

    def __init__(self,
                 text,  # The text to display (can be None)
                 text_colour,  # The colour of the text (can be None)
                 background_colour,  # The colour of the text (can be None)
                 screen_location,  # The position on the screen
                 size,  # The size of the Button
                 event):  # The event trigger by the Button
        """Create a Button."""
        self.text = text
        self.text_colour = text_colour
        self.background_colour = background_colour
        self.screen_location = screen_location
        self.size = size
        self.rect = pygame.Rect(screen_location, size)
        self.event = pygame.event.Event(event)
        self.font = pygame.font.SysFont("comicsansms", 30)

    def display(self, screen):
        """Draw the Goal object on screen, if it has a sprite."""
        # Draw the Button background
        screen.fill(self.background_colour, rect=self.rect)

        # Draw the Button text
        text = self.font.render(self.text,
                                True,
                                self.text_colour)

        # Center the background and text
        text_rect = text.get_rect()
        text_rect.centerx = self.rect.centerx
        text_rect.centery = self.rect.centery

        # Render Button on screen
        screen.blit(text, text_rect)

    def is_mouse_over_button(self, mouse_position):
        """Given a mouse position, return True if mouse over Button."""
        if (mouse_position[0] > self.rect.topleft[0] and
            mouse_position[1] > self.rect.topleft[1] and
            mouse_position[0] < self.rect.bottomright[0] and
            mouse_position[1] < self.rect.bottomright[1]):
            return True
        else:
            return False
