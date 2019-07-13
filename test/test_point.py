"""This class contains the TestPoint class."""
import unittest
from src.Point import Point


class TestPoint(unittest.TestCase):
    """This class unit tests the Point class."""

    def setUp(self):
        """Define two points for use in this test case."""
        self.point1 = Point(2, 3)
        self.point2 = Point(6, 12)

    def test_x(self):
        """Test using the 'x' property."""
        self.assertEqual(self.point1.x, 2)
        self.assertEqual(self.point2.x, 6)

    def test_y(self):
        """Test using the 'y' property."""
        self.assertEqual(self.point1.y, 3)
        self.assertEqual(self.point2.y, 12)

    def test_add(self):
        """Test adding two Point objects."""
        add_result = self.point1 + self.point2
        self.assertTrue(add_result.is_equal_to(Point(8, 15)))

    def test_multiply(self):
        """Test multiplying two Point objects."""
        multiply_result = self.point1 * self.point2
        self.assertTrue(multiply_result.is_equal_to(Point(12, 36)))

    def test_divide(self):
        """Test dividing two Point objects."""
        divide_result = self.point2 / self.point1
        self.assertTrue(divide_result.is_equal_to(Point(3, 4)))

    def test_subtract(self):
        """Test subtracting two Point objects."""
        subtract_result = self.point2 - self.point1
        self.assertTrue(subtract_result.is_equal_to(Point(4, 9)))

    def test_scale(self):
        """Test scaling a Point object."""
        scale_result = self.point1.scale(2)
        self.assertTrue(scale_result.is_equal_to(Point(4, 6)))

    def test_copy(self):
        """Test copying a Point object."""
        copy_result = self.point1.copy()

        # Check the copied Point object is equal to the original but is not
        # the original object.
        self.assertTrue(copy_result.is_equal_to(self.point1))
        self.assertTrue(copy_result is not self.point1)

    def test_is_equal(self):
        """Test the Point is_equal_to method."""
        self.assertTrue(self.point1.is_equal_to(Point(2, 3)))


if __name__ == "__main__":
    unittest.main()
