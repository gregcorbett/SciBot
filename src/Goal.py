"""This file defines the Goal class."""
from src.Component import Component


class Goal(Component):
    """This class defines an individual Goal."""

    def __init__(self,
                 sprite,  # The image to display (can be None)
                 start_logical_position,  # The positon of the Goal
                 step):  # Should be the same as the BeeBot step
        """Create a Goal."""
        # Call superclass constructor
        super().__init__(sprite, start_logical_position, step)

        # True if Goal has been met
        self.has_been_met = False

    def is_equal_to(self, other_component):
        """Compare this Goal for equality with other_goal."""
        if not isinstance(other_component, Goal):
            # A Goal can obviously never be equal to a non Goal
            return False
        return (self.has_been_met == other_component.has_been_met and
                super().is_equal_to(other_component))
