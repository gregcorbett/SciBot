"""This file defines the Goal class."""
from src.Component import Component


class Goal(Component):
    """This class defines an individual Goal."""

    def __init__(self,
                 sprite_list,  # The list of sprites to display.
                 start_logical_position,  # The positon of the Goal
                 step,  # Should be the same as the BeeBot step
                 should_increment_beebot_sprite=False):
        """Create a Goal."""
        # Call superclass constructor
        super().__init__(sprite_list, start_logical_position, step)

        # True if Goal is currently completed.
        self._is_complete = False
        # A marker to indicate that the BeeBot sprite should be incremented
        # after the completion of this Goal.
        self.should_increment_beebot_sprite = should_increment_beebot_sprite

    @property
    def is_complete(self):
        """A "public" getter for the self._is_complete."""
        return self._is_complete

    def complete(self):
        """Mark this Goal as complete and increment the sprite if possible."""
        self._is_complete = True
        if self._sprite_list_index < len(self._sprite_list) - 1:
            self.increment_sprite()

    def reset(self):
        """Reset this Goal."""
        self._is_complete = False
        self._sprite_list_index = 0

    def is_equal_to(self, other_component):
        """Compare this Goal for equality with other_goal."""
        if not isinstance(other_component, Goal):
            # A Goal can obviously never be equal to a non Goal
            return False
        return (self.is_complete == other_component.is_complete and
                super().is_equal_to(other_component))
