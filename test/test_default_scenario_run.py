"""This file contains the TestRunSciBot class."""
import threading
import unittest
import time

import mock
import pygame

from src.GameWindow import GameWindow, RenderingMode


class TestRunSciBot(unittest.TestCase):
    """This test class contains high level integration tests."""

    def setUp(self):
        """Create a test GameWindow and fake Button events."""
        self.test_game_window = GameWindow()
        self.test_game_window.start_rendering()

        # This list is used to generate 'Fake' Button press/release events
        buttons = [("Forward", 950, 420), ("Backward", 950, 680),
                   ("Turn Left", 820, 550), ("Turn Right", 1080, 550),
                   ("Go", 950, 550), ("Reset", 820, 680), ("Clear", 1080, 680)]

        # These dictionaries will store the events
        self.button_down_events = {}
        self.button_up_events = {}

        # Use the above buttons list to generate events
        for button in buttons:
            # 'Fake' Button press
            down_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
            # Simulate a left click
            down_event.button = 1
            # Simulate the position of the click
            down_event.pos = (button[1], button[2])
            # Add this event to the event dictionary,
            # using the corresponding Button text as the key
            self.button_down_events[button[0]] = down_event

            # 'Fake' Button release
            up_event = pygame.event.Event(pygame.MOUSEBUTTONUP)
            # Simulate a left click
            up_event.button = 1
            # Simulate the position of the click
            up_event.pos = (button[1], button[2])
            # Add this event to the event dictionary,
            # using the corresponding Button text as the key
            self.button_up_events[button[0]] = up_event

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

    def test_default_win_clockwise(self):
        """Test the BeeBot can navigate the Default scenario."""
        # These Button presses will navigate the BeeBot to the Goals
        instructions = ['Backward', 'Turn Left', 'Forward', 'Forward',
                        'Turn Right', 'Forward', 'Forward', 'Turn Right',
                        'Forward', 'Go']

        # Simulate Button presses
        for instruction in instructions:
            self._press_button(instruction)

        self._start_timed_logic(timeout_value=45)

    def test_default_win_anti_clockwise(self):
        """Test the BeeBot can navigate the Default scenario."""
        # These Button presses will navigate the BeeBot to the Goals
        instructions = ['Forward', 'Turn Left', 'Forward', 'Forward',
                        'Turn Left', 'Forward', 'Forward', 'Go']

        # Simulate Button presses
        for instruction in instructions:
            self._press_button(instruction)

        self._start_timed_logic(timeout_value=45)

    # Patch so we can tell if fail_run is called
    @mock.patch('src.GameWindow.GameWindow.fail_run')
    def test_default_collison(self, mock_fail_run):
        """Test a failed run due to collisions with Obstacles."""
        # These Button presses will navigate the BeeBot into an Obstacle
        instructions = ['Turn Left', 'Forward', 'Go']

        # Simulate Button presses
        for instruction in instructions:
            self._press_button(instruction)

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
        """Stop rendering the GameWindow."""
        self.test_game_window.rendering_mode = RenderingMode.END_RENDERING

if __name__ == '__main__':
    unittest.main()
