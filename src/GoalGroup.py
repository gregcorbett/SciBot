"""This file defines the GoalGroup class."""


class GoalGroup:
    """This class defines a store for all the goals used."""

    def __init__(self):
        """Create an empty GoalGroup."""
        self.goals = []  # The underlying Goal objects

    def add(self, goal):
        """Add a Goal to the GoalGroup."""
        self.goals.append(goal)

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
