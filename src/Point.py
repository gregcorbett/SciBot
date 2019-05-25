"""This file defines a 2D Point class."""


class Point(tuple):
    """
    This class defines an individual 2D Point.

    The point class should not be used for 2D dimensions like size,
    for that a tuple should be used.
    """

    def __new__(cls, x, y=None):
        """Define a 2D point."""
        if y is None:
            # then assume we were passed a tuple
            return super().__new__(cls, x)

        # Otherwise we assume we were passed two numbers.
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        """Access the x coordinate."""
        return self[0]

    @property
    def y(self):
        """Access the y coordinate."""
        return self[1]

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
        if isinstance(other_point, tuple):
            return Point(self[0] + other_point[0], self[1] + other_point[1])

        return NotImplemented

    def __sub__(self, other_point):
        """Subtract two Point objects coordinate by coordinate."""
        if isinstance(other_point, tuple):
            return Point(self[0] - other_point[0], self[1] - other_point[1])

        return NotImplemented

    def __mul__(self, other_point):
        """Multiply two Point objects coordinate by coordinate."""
        if isinstance(other_point, tuple):
            return Point(self[0] * other_point[0], self[1] * other_point[1])

        return NotImplemented

    def __truediv__(self, other_point):
        """Divide two Point objects coordinate by coordinate."""
        if isinstance(other_point, tuple):
            return Point(self[0] / other_point[0], self[1] / other_point[1])

        return NotImplemented
