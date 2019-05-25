"""This file contains the TestRunSciBot class."""
import threading
import unittest
import time

import mock
import pygame

from src.GameWindow import GameWindow, RenderingMode
from src.Point import Point


class TestRunSciBot(unittest.TestCase):
    """This test class contains high level integration tests."""

    def setUp(self):
        """Create a test GameWindow and fake Button events."""
        self.test_game_window = GameWindow()
        self.test_game_window.start_rendering()

        # This list is used to generate 'Fake' Button press/release events
        buttons = [("Forward", Point(950, 420)),
                   ("Backward", Point(950, 680)),
                   ("Turn Left", Point(820, 550)),
                   ("Turn Right", Point(1080, 550)),
                   ("Go", Point(950, 550)),
                   ("Reset", Point(820, 680)),
                   ("Clear", Point(1080, 680)),
                   ("Stop", Point(950, 550))]

        # These dictionaries will store the events
        self.button_down_events = {}
        self.button_up_events = {}

        # Use the above buttons list to generate events
        for button_text, button_point in buttons:
            # 'Fake' Button press
            down_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
            # Simulate a left click
            down_event.button = 1
            # Simulate the position of the click
            down_event.pos = (button_point.x, button_point.y)
            # Add this event to the event dictionary,
            # using the corresponding Button text as the key
            self.button_down_events[button_text] = down_event

            # 'Fake' Button release
            up_event = pygame.event.Event(pygame.MOUSEBUTTONUP)
            # Simulate a left click
            up_event.button = 1
            # Simulate the position of the click
            up_event.pos = (button_point.x, button_point.y)
            # Add this event to the event dictionary,
            # using the corresponding Button text as the key
            self.button_up_events[button_text] = up_event

    def _press_button(self, button_text):
        """Fake a Button press corresponding to button_text."""
        # Post the Button press event corresponding to button_text
        pygame.event.post(self.button_down_events[button_text])
        # Delay to simulate real user input
        time.sleep(1)
        # Post the Button release event corresponding to button_text
        pygame.event.post(self.button_up_events[button_text])
        # Delay to simulate real user input
        time.sleep(1)

    def _simulate_instructions(self, instructions):
        time.sleep(1)
        # Simulate Button presses
        for instruction in instructions:
            self._press_button(instruction)

    def test_stop_button(self):
        """Test that the Stop Button stops BeeBot movement."""
        # These Button presses will move the BeeBot back exactly one space.
        # As the Stop command will take effect once the BeeBot has processed
        # the first Backward command, so it won't process the second.
        instructions = ['Backward', 'Backward', 'Go', 'Stop']

        self._start_timed_logic(timeout_value=15, expected_to_timeout=True,
                                instructions=instructions)

        position = Point(self.test_game_window.robot.logical_position.x,
                         self.test_game_window.robot.logical_position.y)

        # This is one space below the BeeBot's starting position
        expected_position = Point(3, 2)

        self.assertTrue(position.is_equal_to(expected_position))

    def test_default_win_clockwise(self):
        """Test the BeeBot can navigate the Default scenario."""
        # These Button presses will navigate the BeeBot to the Goals
        instructions = ['Backward', 'Turn Left', 'Forward', 'Forward',
                        'Turn Right', 'Forward', 'Forward', 'Turn Right',
                        'Forward', 'Go']

        self._start_timed_logic(timeout_value=60, instructions=instructions)

    def test_default_win_anti_clockwise(self):
        """Test the BeeBot can navigate the Default scenario."""
        # These Button presses will navigate the BeeBot to the Goals
        instructions = ['Forward', 'Turn Left', 'Forward', 'Forward',
                        'Turn Left', 'Forward', 'Forward', 'Go']

        self._start_timed_logic(timeout_value=60, instructions=instructions)

    # Patch so we can tell if fail_run is called
    @mock.patch('src.GameWindow.GameWindow.fail_run')
    def test_default_collison(self, mock_fail_run):
        """Test a failed run due to collisions with Obstacles."""
        # These Button presses will navigate the BeeBot into an Obstacle
        instructions = ['Turn Left', 'Forward', 'Go']

        # This method should call fail_run given the above instructions
        self._start_timed_logic(timeout_value=15, expected_to_timeout=True,
                                instructions=instructions)

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

    def _start_timed_logic(self, timeout_value=60, expected_to_timeout=False,
                           instructions=None):
        """
        Start a GameWindow that will timeout after timeout_value.

        This method will trigger a test fail if timeout_value was reached
        and expected_to_timeout is False.

        If provided, this method will simulate user input based on the
        provided instructions.
        """
        # Start a timeout thread to catch case where
        # test fails but game loop does not exit
        timeout = threading.Thread(target=self._timeout, args=[timeout_value])
        timeout.start()

        # If this method was passed instructions.
        if instructions:
            # Start a new thread to execute them.
            # _simulate_instructions will wait a second to ensure the
            # GameWindow is visible before simulating instructions
            simulate = threading.Thread(target=self._simulate_instructions,
                                        args=[instructions])
            simulate.start()

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
        """Stop rendering the GameWindow."""
        self.test_game_window.rendering_mode = RenderingMode.END_RENDERING

if __name__ == '__main__':
    unittest.main()
