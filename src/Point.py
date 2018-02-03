"""This file defines a 2D Point class."""


class Point():
    """
    This class defines an individual 2D Point.

    The point class should not be used for 2D dimensions like size,
    for that a tuple should be used.
    """

    def __init__(self, x, y=None):
        """Define a 2D point."""
        if y is None:  # then assume we were passed a tuple
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y

    def is_equal_to(self, other_point):
        """True if both x and y are equal in self and other_point."""
        return self.x == other_point.x and self.y == other_point.y

    def scale(self, multipler):
        """Return a point such that x and y are multipled by multipler."""
        return Point(self.x * multipler, self.y * multipler)

    def copy(self):
        """Return a copy of this Point object."""
        return Point(self.x, self.y)

    def __add__(self, other_point):
        """Add two Point objects coordinate by coordinate."""
        return (self.x + other_point.x, self.y + other_point.y)

    def __sub__(self, other_point):
        """Subtract two Point objects coordinate by coordinate."""
        return Point(self[0] - other_point[0], self[1] - other_point[1])

    def __mul__(self, other_point):
        """Multiply two Point objects coordinate by coordinate."""
        return (self.x * other_point.x, self.y * other_point.y)

    def __truediv__(self, other_point):
        """Divide two Point objects coordinate by coordinate."""
        return (self.x / other_point.x, self.y / other_point.y)
