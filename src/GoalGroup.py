"""This file defines the GoalGroup class."""


class GoalGroup:
    """This class defines a store for all the goals used."""

    def __init__(self, ordered=True):
        """Create an empty GoalGroup."""
        self.goals = []  # The underlying Goal objects
        self.is_ordered = ordered
        if self.is_ordered:
            self._goal_ptr = 0

    def add(self, goal):
        """Add a Goal to the GoalGroup."""
        self.goals.append(goal)

    def display(self, screen):
        """Draw all Goal objects in the GoalGroup."""
        for goal in self.goals:
            goal.display(screen)

    def get_current_goal(self):
        """If Goal's are ordered, return the current goal."""
        # GoalGroup must be ordered for there to be a current goal
        if self.is_ordered:
            return self.goals[self._goal_ptr]
        else:
            raise NotImplementedError

    def increment_pointer(self):
        """If Goal's are ordered, increment the current goal."""
        # GoalGroup must be ordered for there to be a _goal_ptr
        if self.is_ordered:
            self._goal_ptr = self._goal_ptr + 1
        else:
            raise NotImplementedError

    def have_all_goals_been_met(self):
        """True iff all the Goal objects in the GoalGroup have been met."""
        for goal in self.goals:
            if not goal.has_been_met:
                return False
        return True

    def reset_all_goals(self):
        """Set all Goals to not been met."""
        for goal in self.goals:
            goal.has_been_met = False
        # if Goals are ordered, move ptr back to start of GoalGroup
        if self.is_ordered:
            self._goal_ptr = 0
