"""This file contains the TestBeeBot class."""
import unittest
import pygame


from src.BeeBot import BeeBot, Heading
from src.CustomEvent import CustomEvent
from src.Point import Point
from src.Scenario import Scenario


class TestBeeBot(unittest.TestCase):
    """This test class unit tests the BeeBot class."""

    def setUp(self):
        """
        Create a minimal Scenario and use it to create a BeeBot.

        The Scenario is 5x5 (logical and pixel size)
        with the BeeBot in the centre, and no Obstacles or Goals.
        """
        # Create the minimal Scenario
        test_scenario = Scenario('Test')
        test_scenario.set_board_step(1)
        test_scenario.set_logical_width(5)
        test_scenario.set_logical_height(5)
        test_scenario.set_beebot_start_position(2, 2)
        test_scenario.set_beebot_sprite('img/Default/robot.jpg')
        # Create the test BeeBot
        self.test_robot = BeeBot(test_scenario)

    def test_add_to_memory(self):
        """Test the add_to_memory method."""
        # Create an event
        event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP)
        # Add it to the BeeBot's memory
        self.test_robot.add_to_memory(event)
        # Assert the BeeBot's memory only contains that event
        self.assertEqual(len(self.test_robot.memory), 1)
        [memory_event] = self.test_robot.memory
        self.assertEqual(memory_event.type, CustomEvent.MOVE_BEEBOT_UP)

    def test_clear_memory(self):
        """Test the clear_memory method."""
        # Create an event
        event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP)
        # Add it to the BeeBot's memory
        self.test_robot.add_to_memory(event)
        # Clear the BeeBot's memory
        self.test_robot.clear_memory()
        # Assert the BeeBot's memory is empty
        self.assertEqual(len(self.test_robot.memory), 0)

    def test_push_out_memory(self):
        """Test the push_out_memory method."""
        try:
            # Need to initaite pygame as we will use the event loop to confirm
            # proper function of the push_out_memory function.
            pygame.init()
            # Create events
            events = [pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP),
                      pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN),
                      # We will use this event to prove we are removing
                      # events from the queue
                      pygame.event.Event(pygame.NOEVENT)]

            # Add all events to the BeeBot's memory
            for event in events:
                self.test_robot.add_to_memory(event)

            # Push out all instructions
            for event in events:
                self.test_robot.push_out_memory()

            # Check the polled events match the events pushed
            for event in events:
                event_polled = pygame.event.poll()
                self.assertEqual(event, event_polled)

        # No matter what happens, exit pygame
        finally:
            pygame.quit()

    def test_turn_left(self):
        """Test the move and move_left methods."""
        # Set the BeeBot's Heading
        self.test_robot.heading = Heading.NORTH
        # Create an event
        move_left_event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_left_event)
        self.assertEqual(self.test_robot.heading, Heading.WEST)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_left_event)
        self.assertEqual(self.test_robot.heading, Heading.SOUTH)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_left_event)
        self.assertEqual(self.test_robot.heading, Heading.EAST)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_left_event)
        self.assertEqual(self.test_robot.heading, Heading.NORTH)

    def test_turn_right(self):
        """Test the move and move_right methods."""
        # Set the BeeBot's Heading
        self.test_robot.heading = Heading.NORTH
        # Create an event
        move_right_event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_right_event)
        self.assertEqual(self.test_robot.heading, Heading.EAST)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_right_event)
        self.assertEqual(self.test_robot.heading, Heading.SOUTH)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_right_event)
        self.assertEqual(self.test_robot.heading, Heading.WEST)

        # Move the BeeBot left and check it's heading is as expected
        self.test_robot.move(move_right_event)
        self.assertEqual(self.test_robot.heading, Heading.NORTH)

    def test_move_forward(self):
        """Test the move and move_forward methods."""
        # test cases for this test are a tuple consisting of the BeeBot's
        #  Heading and the BeeBot's new position after
        # moving forward with that Heading
        test_cases = [(Heading.NORTH, Point(2, 1)),
                      (Heading.EAST, Point(3, 2)),
                      (Heading.SOUTH, Point(2, 3)),
                      (Heading.WEST, Point(1, 2))]

        # Create an event
        move_forward_event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP)
        for test_case in test_cases:
            # Set the BeeBot's setting
            self.test_robot.heading = test_case[0]
            # Pass the event to the move method
            self.test_robot.move(move_forward_event)
            # Assert the BeeBot's current position is what we expect it to be
            self.assertTrue(
                self.test_robot.logical_position.is_equal_to(test_case[1])
                )
            # Reset the BeeBot's position so each test
            # in the loop is independant
            self.test_robot.reset_position()

    def test_move_backward(self):
        """Test the move and move_backward methods."""
        # test cases for this test are a tuple consisting of the BeeBot's
        #  Heading and the BeeBot's new position after
        # moving backward with that Heading
        test_cases = [(Heading.NORTH, Point(2, 3)),
                      (Heading.EAST, Point(1, 2)),
                      (Heading.SOUTH, Point(2, 1)),
                      (Heading.WEST, Point(3, 2))]

        # Create an event
        move_backward_event = pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN)
        for test_case in test_cases:
            # Set the BeeBot's setting
            self.test_robot.heading = test_case[0]
            # Pass the event to the move method
            self.test_robot.move(move_backward_event)
            # Assert the BeeBot's current position is what we expect it to be
            self.assertTrue(
                self.test_robot.logical_position.is_equal_to(test_case[1])
                )
            # Reset the BeeBot's position so each test
            # in the loop is independant
            self.test_robot.reset_position()

if __name__ == '__main__':
    unittest.main()
