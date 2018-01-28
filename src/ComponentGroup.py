"""This file defines the ComponentGroup class."""


class ComponentGroup:
    """This class defines a store for all the Components used."""

    def __init__(self):
        """Create an empty ComponentGroup."""
        # The underlying Component objects
        self.components = []

    def add(self, component):
        """Add a Component to the ComponentGroup."""
        self.components.append(component)

    def display(self, screen):
        """Draw all Component objects in the ComponentGroup."""
        for component in self.components:
            component.display(screen)

    def is_equal_to(self, other_component_group):
        """Compare the two ComponentGroups for unordered equality."""
        if len(self.components) is not len(other_component_group.components):
            # Then we can return quickly as they are clearly not equal
            return False

        # The below comparsion assumes both ComponentGroups are the same size.
        # To be as general as possible, for each element in self.components
        # we check how many times it appears in both self.components and
        # other_component_group.components. If the counts are unequal,
        # the ComponentGroup are different.
        for i in range(0, len(self.components)):
            elem = self.components[i]

            # (Re)set variables to store the element counts
            self_count = 0
            other_count = 0

            # Look for elem in self.components
            self_count = self._count_occurrences(elem)

            # Look for elem in other_component_group.components
            other_count = self._count_occurrences(elem, other_component_group)

            # If the counters aren't equal, the ComponentGroups can't be equal.
            if self_count != other_count:
                return False

        # If we get here, then the ComponentGroups are assumed to be equal.
        return True

    def _count_occurrences(self, element, component_group=None):
        """
        Count the number of times the element appears in component_group.

        If no ComponentGroup is provided, the method will check self.
        """
        if component_group is None:
            component_group = self

        count = 0
        for j in range(0, len(component_group.components)):
            if element.is_equal_to(component_group.components[j]):
                # Each time elem is present, increment counter
                count += 1

        return count
