"""This file defines the GoalGroup class."""

from src.ComponentGroup import ComponentGroup


class GoalGroup(ComponentGroup):
    """This class defines a store for all the goals used."""

    def __init__(self, ordered=True):
        """Create an empty GoalGroup."""
        super().__init__()

        self.is_ordered = ordered
        if self.is_ordered:
            self._goal_ptr = 0

    def get_current_goal(self):
        """If Goal's are ordered, return the current goal."""
        # GoalGroup must be ordered for there to be a current goal
        if self.is_ordered:
            return self.components[self._goal_ptr]

        # Raised if called on an unordered GoalGroup
        # This method has no meaning under such circumstances
        raise ValueError("Cannot call method on unordered GoalGroup.")

    def increment_pointer(self):
        """If Goal's are ordered, increment the current goal."""
        # GoalGroup must be ordered for there to be a _goal_ptr
        if self.is_ordered:
            self._goal_ptr = self._goal_ptr + 1
        else:
            # Raised if called on an unordered GoalGroup
            # This method has no meaning under such circumstances
            raise ValueError("Cannot call method on unordered GoalGroup.")

    def have_all_goals_been_met(self):
        """True iff all the Goal objects in the GoalGroup have been met."""
        for goal in self.components:
            if not goal.has_been_met:
                return False
        return True

    def reset_all_goals(self):
        """Set all Goals to not been met."""
        for goal in self.components:
            goal.has_been_met = False
        # if Goals are ordered, move ptr back to start of GoalGroup
        if self.is_ordered:
            self._goal_ptr = 0

    def is_equal_to(self, other_component_group):
        """Compare this GoalGroup for equality with other_component_group."""
        if not isinstance(other_component_group, GoalGroup):
            # An GoalGroup can obviously never be equal to a non GoalGroup.
            return False

        if self.is_ordered:
            # Then return the ordered check
            return self._is_equal_to_ordered(other_component_group)

        # If we get here, use the base ComponentGroup comparison.
        return super().is_equal_to(other_component_group)

    def _is_equal_to_ordered(self, ordered_goal_group):
        """
        Compare the two GoalGroups for ordered equality.

        It does not check that either GoalGroup is ordered.
        """
        if len(self.components) is not len(ordered_goal_group.components):
            # Then we can return quickly as they are clearly not equal
            return False

        # The below comparsion assumes both GoalGroups are the same size.
        # We can simply check that the elements are equal in order.
        for i in range(0, len(self.components)):
            if not self.components[i].is_equal_to(
                    ordered_goal_group.components[i]):
                return False

        # If we get here, then the GoalGroups are assumed to be equal.
        return True
