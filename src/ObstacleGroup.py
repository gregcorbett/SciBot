"""This file defines the ObstacleGroup class."""


class ObstacleGroup:
    """This class defines a store for all the goals used."""

    def __init__(self):
        """Create an empty ObstacleGroup."""
        self.obstacles = []  # The underlying Goal objects

    def add(self, obstacle):
        """Add a Obstacle to the ObstacleGroup."""
        self.obstacles.append(obstacle)

    def display(self, screen):
        """Draw all Obstacle objects in the ObstacleGroup."""
        for obstacle in self.obstacles:
            obstacle.display(screen)

    def is_equal_to(self, other_obstacle_group):
        """Compare this ObstacleGroup for equality with other_obstacle_group."""
        for i in range(0, len(self.obstacles)):
            if not self.obstacles[i].is_equal_to(other_obstacle_group.obstacles[i]):
                return False
        return True
