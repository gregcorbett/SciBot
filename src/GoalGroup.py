"""This file defines the GoalGroup class."""


class GoalGroup:
    """This class defines a store for all the _goals used."""

    def __init__(self):
        """Create an empty GoalGroup."""
        self.goal_count = 0  # The number of Goal objects in the group
        self._goals = {}  # The underlying Goal objects
        self._goal_ptr = 0  # A pointer for manipulating Goal objects

    def add(self, goal):
        """Add a Goal to the GoalGroup."""
        self._goals[self.goal_count] = goal
        self.goal_count = self.goal_count + 1

    def display(self, screen):
        """Draw all Goal objects in group."""
        if self._goal_ptr < self.goal_count:
            self._goals[self._goal_ptr].display(screen)
