"""This file defines the GoalGroup class."""


class GoalGroup:
    """This class defines a store for all the _goals used."""

    def __init__(self):
        """Create an empty GoalGroup."""
#        self.goal_count = 0  # The number of Goal objects in the group
        self.goals = []  # The underlying Goal objects
#        self._goal_ptr = 0  # A pointer for manipulating Goal objects

    def add(self, goal):
        """Add a Goal to the GoalGroup."""
        self.goals.append(goal)
#        self.goal_count = self.goal_count + 1

    def display(self, screen):
        """Draw all Goal objects in the GoalGroup."""
        for goal in self.goals:
            goal.display(screen)

    def have_all_goals_been_met(self):
        """True iff all the Goal objects in the GoalGroup have been met."""
        for goal in self.goals:
            if not goal.has_been_met:
                print("Goal has not been met!")
                return False
        print("Goal has been met!")
        return True

    def reset_all_goals(self):
        """True iff all Goal objects have been met."""
        for goal in self.goals:
            goal.has_been_met = False
