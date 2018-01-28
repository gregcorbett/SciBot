"""This file defines the ObstacleGroup class."""

from src.ComponentGroup import ComponentGroup


class ObstacleGroup(ComponentGroup):
    """This class defines a store for all the goals used."""

    def is_equal_to(self, other_component_group):
        """Compare this ObstacleGroup is equal to other_component_group."""
        if not isinstance(other_component_group, ObstacleGroup):
            # An ObstacleGroup can obviously never
            # be equal to a non ObstacleGroup.
            return False

        # If we get here, use the base ComponentGroup comparison.
        return super().is_equal_to(other_component_group)
