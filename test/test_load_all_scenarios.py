"""This file contains the TestLoadScenario class."""
import os
import unittest

from src.GameWindow import GameWindow


class TestLoadScenaro(unittest.TestCase):
    """This test class can be used to add tests for loading scenarios."""

    def setUp(self):
        """Create a new GameWindow."""
        self.test_game_window = GameWindow()


def make_test_load_scenario(scenario_file):
    """Generate test methods for loading scenario."""
    def test_load_scenario(self):
        """Load a scenario."""
        scenario_path = os.path.abspath(os.path.join(".", "scenarios",
                                                     scenario_file))

        self.test_game_window.scenario = scenario_path
        self.test_game_window.load_scenario()
    return test_load_scenario


# Make a test case for each scenario found in the scenario directory
for scenario in os.listdir(os.path.abspath(os.path.join(".", "scenarios"))):
    # Check it is a scibot file (based off the extension)
    if ".scibot" not in scenario:
        # If it is not a scibot file, then skip this file
        continue

    # Add a test to load the scenario to the TestLoadScenaro class
    test_method = make_test_load_scenario(scenario)
    test_method.__name__ = "test_load_%s_scenario" % scenario[:-7]
    setattr(TestLoadScenaro, test_method.__name__, test_method)

if __name__ == '__main__':
    unittest.main()
