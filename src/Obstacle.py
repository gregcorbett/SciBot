"""This file defines the Object class."""
from src.Component import Component


class Obstacle(Component):
    """This class defines an individual Obstacle."""

    def is_equal_to(self, other_component):
        """Compare this Obstacle for equality with other_component."""
        if not isinstance(other_component, Obstacle):
            # An Obstacle can obviously never be equal to a non Obstacle
            return False
        return super().is_equal_to(other_component)
