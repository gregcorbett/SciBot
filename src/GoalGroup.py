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
            # Raised if called on an unordered GoalGroup
            # This method has no meaning under such circumstances
            raise ValueError("GoalGroup not ordered.")

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

    def is_equal_to(self, other_goal_group):
        """Compare this GoalGroup for equality with other_goal_group."""
        if self.is_ordered and not other_goal_group.is_ordered:
            # Then we can return False quickly as a ordered GoalGroup is
            # different to an unordered GoalGroup.
            return False

        if len(self.goals) is not len(other_goal_group.goals):
            # Then we can return quickly as they are clearly not equal
            return False

        if self.is_ordered:
            # Then we can simply check that the elements are equal in order.
            for i in range(0, len(self.goals)):
                if not self.goals[i].is_equal_to(other_goal_group.goals[i]):
                    return False

        else:
            # Then to be as general as possible, for each element in self.goals
            # we check how many times it appears in both self.goals and
            # other_goal_group.goals. If the counts are unequal,
            # the GoalGroups are different.
            for i in range(0, len(self.goals)):
                elem = self.goals[i]

                # (Re)set variables to store the element counts
                self_count = 0
                other_count = 0

                # Look for elem in self.goals
                for j in range(0, len(self.goals)):
                    if elem.is_equal_to(self.goals[j]):
                        # Each time elem is present, increment counter
                        self_count += 1

                # Look for elem in other_goal_group.goals
                for k in range(0, len(other_goal_group.goals)):
                    if elem.is_equal_to(other_goal_group.goals[k]):
                        # Each time elem is present, increment counter
                        other_count += 1

                # If the counters aren't equal, the GoalGroups can't be equal.
                if self_count != other_count:
                    return False

        # If we get here, then the GoalGroups are assumed to be equal.
        return True
