"""This file defines the main GameWindow and the Enum RenderingMode."""


from threading import Thread
from pickle import load
from time import sleep
from enum import Enum
import sys
import pygame
import pygame.freetype
from src.BeeBot import BeeBot, Heading
from src.Board import Board
from src.CustomEvent import CustomEvent
from src.Scenario import Scenario


class RenderingMode(Enum):
    """A class of Enums determining how the GameWindow will render."""

    TITLE_SCREEN = 1
    CHOOSE_SCENARIO = 2
    NORMAL = 3
    WIN_SCREEN = 4
    FAIL_SCREEN = 5
    END_RENDERING = 6


class GameWindow(Thread):
    """This class defines the main GameWindow."""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    FRAMES_PER_SECOND = 24

    def __init__(self):
        """Initiate the GameWindow."""
        pygame.init()

        # Define vars here
        self.rendering_mode = None

        self.scenario = None

        self.step = None
        self.height = None
        self.width = None

        self.board = None
        self.size = None

        self.robot = None

        self.screen = None

        self.clock = None

        self.font = None

        # Call the superclass constructor
        Thread.__init__(self)

    def start_rendering(self):
        """Change rendering_mode to TITLE_SCREEN and begin rendering."""
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.rendering_mode = RenderingMode.TITLE_SCREEN
        self.start()  # Runs the run method.

    def run(self):
        """Run the rendering engine."""
        while True:
            if self.rendering_mode is RenderingMode.TITLE_SCREEN:
                # For now, we will let runSciBot drive the rendering
                pass

            elif self.rendering_mode is RenderingMode.CHOOSE_SCENARIO:
                # For now, we will let runSciBot drive the rendering
                pass

            elif self.rendering_mode is RenderingMode.NORMAL:
                # Display the Board and BeeBot
                self.display_board_and_beebot()

                # Update display
                pygame.display.update()

                # Limits the render to FRAMES_PER_SECOND
                self.clock.tick(GameWindow.FRAMES_PER_SECOND)

            elif self.rendering_mode is RenderingMode.WIN_SCREEN:
                # Display some text
                self.display_text('Hooray you won!! Thanks for playing!',
                                  GameWindow.WHITE,
                                  GameWindow.RED)

                # Update display
                pygame.display.update()

                # Limits the render to FRAMES_PER_SECOND
                self.clock.tick(GameWindow.FRAMES_PER_SECOND)

            elif self.rendering_mode is RenderingMode.FAIL_SCREEN:
                # Display some text
                self.display_text('Oh no, you crashed! Try again!',
                                  GameWindow.WHITE,
                                  GameWindow.BLACK)

                # Update display
                pygame.display.update()

                # Limits the render to FRAMES_PER_SECOND
                self.clock.tick(GameWindow.FRAMES_PER_SECOND)

            elif self.rendering_mode is RenderingMode.END_RENDERING:
                break  # Let the renderer die

    def choose_scenario(self):
        """Somehow Choose a Scenario."""

        scenarioPath = input("Please enter path and file name of scenario: ")
        if scenarioPath is "":
            scenarioPath = "./scenarios/Default.scibot"

        self.scenario = load(open(scenarioPath,
                                  "rb"))

    def load_scenario(self):
        """Load the chosen Scenario."""
        self.step = self.scenario.get_element('BoardStep')
        self.height = self.scenario.get_element('LogicalHeight')*self.step
        self.width = self.scenario.get_element('LogicalWidth')*self.step

        self.board = Board(self.scenario)
        self.size = (self.width, self.height)

        self.robot = BeeBot(self.scenario)

        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

    def start_scenario(self):
        """Start the Scenario."""
        # Go to NORMAL rendering
        self.rendering_mode = RenderingMode.NORMAL
        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                self.rendering_mode = RenderingMode.END_RENDERING
                sleep(1)
                pygame.quit()
                sys.exit()

            if event.type == CustomEvent.RUN_FAIL:
                self.robot.heading = Heading.FAIL
                sleep(1)
                self.rendering_mode = RenderingMode.FAIL_SCREEN
                sleep(2)
                self.rendering_mode = RenderingMode.NORMAL
                self.robot.reset_position()
                self.robot.clear_memory()
                self.board.goal_group.reset_all_goals()

            if event.type == CustomEvent.RUN_WIN:
                sleep(1)
                self.rendering_mode = RenderingMode.WIN_SCREEN
                sleep(2)
                self.rendering_mode = RenderingMode.END_RENDERING
                sleep(1)
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                self.handle_key_press(event)

            # If the event is a movement event
            # Move the BeeBot.
            if event.type >= CustomEvent.MOVE_BEEBOT_UP and event.type <= CustomEvent.MOVE_BEEBOT_RIGHT:
                self.robot.move(event)
                self.check_for_obstacle_collisions()
                self.check_for_goal_collisions()

    def check_for_goal_collisions(self):
        """Check if the BeeBot is currently on a Goal."""
        # If so, mark that Goal as met.
        # If all Goals met, push a CustomEvent.RUN_WIN.
        for goal in self.board.goal_group.goals:
            if self.robot.logical_position_x == goal.logical_position_x and self.robot.logical_position_y == goal.logical_position_y:
                goal.has_been_met = True
                if self.board.goal_group.have_all_goals_been_met():
                    # clear any remaining events
                    pygame.event.clear()
                    # push a win event
                    pygame.event.post(pygame.event.Event(CustomEvent.RUN_WIN))

    def check_for_obstacle_collisions(self):
        """Check if the BeeBot is currently on a Obstacle."""
        # If so, push a CustomEvent.RUN_FAIL.
        for obstacle in self.board.obstacle_group.obstacles:
            if self.robot.logical_position_x == obstacle.logical_position_x and self.robot.logical_position_y == obstacle.logical_position_y:
                # clear any remaining events
                pygame.event.clear()
                # push a fail event
                pygame.event.post(pygame.event.Event(CustomEvent.RUN_FAIL))

    def display_board_and_beebot(self):
        """Display the Board and BeeBot."""
        if self.board is not None:
            self.board.display(self.screen)
        if self.robot is not None:
            self.robot.display(self.screen)

    def display_text(self, text, text_colour, background_colour):
        """Display text on background_colour."""
        self.screen.fill(background_colour)
        text = self.font.render(text,
                                True,
                                text_colour,
                                background_colour)

        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery
        self.screen.blit(text, text_rect)

    def handle_key_press(self, event):
        """Convert key press into game logic."""
        # If the event is an arrow key, store
        # a movement event in the BeeBot.
        if event.key == pygame.K_UP:
            new_event = CustomEvent.MOVE_BEEBOT_UP
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if event.key == pygame.K_DOWN:
            new_event = CustomEvent.MOVE_BEEBOT_DOWN
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if event.key == pygame.K_LEFT:
            new_event = CustomEvent.MOVE_BEEBOT_LEFT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if event.key == pygame.K_RIGHT:
            new_event = CustomEvent.MOVE_BEEBOT_RIGHT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        # if the event is the space bar,
        # reset the BeeBot's position and clears any met goals.
        # it doesn't clear the memory!
        if event.key == pygame.K_SPACE:
            self.robot.reset_position()
            self.board.goal_group.reset_all_goals()

        # if the event is the X key, clear the BeeBot's memory
        if event.key == ord('x') or event.key == ord('X'):
            self.robot.memory = []

        # if the event is the G key, push stored movement
        # events into the event queue.
        if event.key == ord('g') or event.key == ord('G'):
            self.robot.push_out_memory()
