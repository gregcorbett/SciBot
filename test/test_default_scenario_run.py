"""This file contains the TestRunSciBot class."""
import threading
import unittest
import time

import mock
import pygame

from src.GameWindow import GameWindow, RenderingMode
from src.CustomEvent import CustomEvent


class TestRunSciBot(unittest.TestCase):
    """This test class contains high level integration tests."""

    # Set this to True to render the test cases as they are run
    RENDER = False

    def setUp(self):
        """Create a test GameWindow."""
        self.test_game_window = GameWindow()
        if self.RENDER:
            self.test_game_window.start_rendering()

    def test_default_win(self):
        """Test the BeeBot can navigate the Default scenario."""
        # These instrctions will navigate the BeeBot to the Goals
        instructions = [pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP)]

        # Post instructions to the pygame event queue
        for instruction in instructions:
            pygame.event.post(instruction)

        self._start_timed_logic()

    # Patch so we can tell if fail_run is called
    @mock.patch('src.GameWindow.GameWindow.fail_run')
    def test_default_collison(self, mock_fail_run):
        """Test a failed run due to collisions with Obstacles."""
        # These instructions will navigate the BeeBot into an Obstacle
        instructions = [pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT),
                        pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP)]

        # Post instructions to the pygame event queue
        for instruction in instructions:
            pygame.event.post(instruction)

        # This method should call fail_run given the above instructions
        self._start_timed_logic(timeout_value=15, expected_to_timeout=True)

        # Assert fail_run was called exactly once
        self.assertEqual(mock_fail_run.call_count, 1)

    def _timeout(self, timeout_value=60):
        """Helper method to exit the game after timeout_value."""
        counter = 0
        while counter < timeout_value:
            time.sleep(1)
            counter = counter + 1
        # After the timeout_value has been reached, stop the game logic
        self.test_game_window._logic_running = False

    def _start_timed_logic(self, timeout_value=60, expected_to_timeout=False):
        """
        Start a GameWindow that will timeout after timeout_value.

        This method will trigger a test fail if timeout_value was reached
        and expected_to_timeout is False.
        """
        # Start a timeout thread to catch case where
        # test fails but game loop does not exit
        timeout = threading.Thread(target=self._timeout, args=[timeout_value])
        timeout.start()

        # Start the game logic
        self.test_game_window.start_logic(scenario='Default')

        # Did the game logic finish (before the time out)
        if timeout.isAlive():
            # Wait for timeout thread to end before finishing test
            # Avoids 'Zombie'-threads lingering beyond test case
            timeout.join(timeout_value)
        elif expected_to_timeout:
            # The we want to do some extra checks, perhaps assert a
            # particular method was called, so do nothing
            pass
        else:
            # Then we assume the test has failed,
            self.fail('Timeout Reached.')

    def tearDown(self):
        """Stop rendering, if applicable."""
        if self.RENDER:
            self.test_game_window.rendering_mode = RenderingMode.END_RENDERING

if __name__ == '__main__':
    unittest.main()
