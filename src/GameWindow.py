"""This file defines the main GameWindow and the Enum RenderingMode."""


from threading import Thread
from pickle import load
from time import sleep
from enum import Enum
import sys
import pygame
from src.BeeBot import BeeBot, Heading
from src.Board import Board
from src.Button import Button
from src.ButtonGroup import ButtonGroup
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
    GREY = (100, 100, 100)
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
                self.screen.fill(GameWindow.GREY)

                # Display the Board and BeeBot
                self.board.display(self.screen)
                self.robot.display(self.screen)

                # Display any Buttons
                self.buttons.display(self.screen)

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
        while True:
            try:
                scenario_path = input("Choose a Scenario: ")
                if scenario_path is "":
                    scenario_path = "./scenarios/Default.scibot"
                elif ".scibot" not in scenario_path:
                    scenario_path = "./scenarios/" + scenario_path + ".scibot"

                self.scenario = load(open(scenario_path, "rb"))
                break  # only get here if there is no exception

            except FileNotFoundError:
                print("Could not find file: %s, try again!" % scenario_path)

            except OSError:
                print("OSError! Try again!")
                print("HINT: Possibly remove \", as they arent needed.")

    def load_scenario(self):
        """Load the chosen Scenario."""
        self.step = self.scenario.get_element('BoardStep')
        self.height = self.scenario.get_element('LogicalHeight')*self.step
        self.width = self.scenario.get_element('LogicalWidth')*self.step

        self.board = Board(self.scenario)

        self.robot = BeeBot(self.scenario)

        self.clock = pygame.time.Clock()

        buttons_on_the_left = True

        self.create_buttons(buttons_on_the_left)

        if buttons_on_the_left:
            self.size = (self.width + 400, self.height)
        else:
            self.size = (self.width, self.height + 400)

        self.screen = pygame.display.set_mode(self.size)


    def create_buttons(self, buttons_on_the_left):
        """Helper method to populate ButtonGroup."""
        self.buttons = ButtonGroup()

        if buttons_on_the_left:
            forward_button = Button('Forward',
                                    GameWindow.BLACK,
                                    GameWindow.WHITE,
                                    (self.width + 140, float(self.height)/2 - 190),
                                    (120,120))

            self.buttons.add(forward_button)

            backward_button = Button('Backward',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (self.width + 140, float(self.height)/2 + 70),
                                     (120,120))

            self.buttons.add(backward_button)

            turn_left_button = Button('Turn Left',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (self.width + 10, float(self.height)/2 - 60),
                                     (120,120))

            self.buttons.add(turn_left_button)

            turn_right_button = Button('Turn Right',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (self.width + 270, float(self.height)/2 - 60),
                                     (120,120))

            self.buttons.add(turn_right_button)

            go_button = Button('Go',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               (self.width + 140, float(self.height)/2 - 60),
                               (120,120))

            self.buttons.add(go_button)



            reset_button = Button('Reset',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (self.width + 10, float(self.height)/2 + 70),
                                     (120,120))

            self.buttons.add(reset_button)

            clear_button = Button('Clear',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               (self.width + 270, float(self.height)/2 + 70),
                               (120,120))

            self.buttons.add(clear_button)

        else:
            forward_button = Button('Forward',
                                    GameWindow.BLACK,
                                    GameWindow.WHITE,
                                    (float(self.width)/2 - 60, self.height + 10),
                                    (120,120))

            self.buttons.add(forward_button)

            backward_button = Button('Backward',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (float(self.width)/2 - 60, self.height + 270),
                                     (120,120))

            self.buttons.add(backward_button)

            turn_left_button = Button('Turn Left',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (float(self.width)/2 - 190, self.height + 140),
                                     (120,120))

            self.buttons.add(turn_left_button)

            turn_right_button = Button('Turn Right',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (float(self.width)/2 + 70, self.height + 140),
                                     (120,120))

            self.buttons.add(turn_right_button)

            go_button = Button('Go',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               (float(self.width)/2 - 60, self.height + 140),
                               (120,120))

            self.buttons.add(go_button)



            reset_button = Button('Reset',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     (float(self.width)/2 - 190, self.height + 270),
                                     (120,120))

            self.buttons.add(reset_button)

            clear_button = Button('Clear',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               (float(self.width)/2 + 70, self.height + 270),
                               (120,120))

            self.buttons.add(clear_button)


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
                self.robot.sprite = self.robot.fail_sprite
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
                sys.exit()

            if event.type == pygame.KEYDOWN:
                self.handle_key_press(event)

            # If the event is a movement event
            # Move the BeeBot.
            if (
               event.type >= CustomEvent.MOVE_BEEBOT_UP and
               event.type <= CustomEvent.MOVE_BEEBOT_RIGHT
               ):
                self.robot.move(event)
                self.check_for_obstacle_collisions()
                self.check_for_goal_collisions()
                self.check_for_off_map()

            # If the event is a left mouse button up
            # assume it is a button press
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button = self.buttons.get_appropriate_button(event.pos)
                if button is not None and button.swapped:
                    button.swap_colours()
                    self.handle_button_press(button)
                else:
                    self.buttons.unswap_all()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                button = self.buttons.get_appropriate_button(event.pos)
                if button is not None:
                    button.swap_colours()


    def check_for_goal_collisions(self):
        """Check if the BeeBot is currently on a Goal."""
        # If so, mark that Goal as met.
        # If all Goals met, push a CustomEvent.RUN_WIN.
        if self.board.goal_group.is_ordered:
            goal = self.board.goal_group.get_current_goal()
            if self.robot.logical_position.is_equal_to(goal.logical_position):
                goal.has_been_met = True
                self.board.goal_group.increment_pointer()

        else:
            for goal in self.board.goal_group.goals:
                if self.robot.logical_position.is_equal_to(goal.logical_position):
                    goal.has_been_met = True

        if self.board.goal_group.have_all_goals_been_met():
            # clear any remaining events
            pygame.event.clear()
            # push a win event
            pygame.event.post(pygame.event.Event(CustomEvent.RUN_WIN))

    def fail_run(self):
        # clear any remaining events
        pygame.event.clear()
        # push a fail event
        pygame.event.post(pygame.event.Event(CustomEvent.RUN_FAIL))

    def check_for_obstacle_collisions(self):
        """Check if the BeeBot is currently on a Obstacle."""
        # If so, push a CustomEvent.RUN_FAIL.
        for obstacle in self.board.obstacle_group.obstacles:
            if self.robot.logical_position.is_equal_to(obstacle.logical_position):
                self.fail_run()

    def check_for_off_map(self):
        """Check if the BeeBot is off the map"""
        if self.robot.logical_position.x not in range(0, self.board.logical_board_width):
            self.fail_run()
        elif self.robot.logical_position.y not in range(0, self.board.logical_board_height):
            self.fail_run()

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

    def store_movement(self, movement):
        """Store a movement in the BeeBot."""
        if movement == 'Forward':
            new_event = CustomEvent.MOVE_BEEBOT_UP
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Left':
            new_event = CustomEvent.MOVE_BEEBOT_LEFT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Right':
            new_event = CustomEvent.MOVE_BEEBOT_RIGHT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Backward':
            new_event = CustomEvent.MOVE_BEEBOT_DOWN
            self.robot.add_to_memory(pygame.event.Event(new_event))

    def handle_button_press(self, button):
        """Convert button press into game logic."""
        if button.text == 'Forward':
            self.store_movement('Forward')

        if button.text == 'Turn Left':
            self.store_movement('Left')

        if button.text == 'Turn Right':
            self.store_movement('Right')

        if button.text == 'Backward':
            self.store_movement('Backward')

        if button.text == 'Reset':
            self.robot.reset_position()
            self.board.goal_group.reset_all_goals()

        if button.text == 'Clear':
            self.robot.memory = []

        if button.text == 'Go':
            self.robot.push_out_memory()

    def handle_key_press(self, event):
        """Convert key press into game logic."""
        # If the event is an arrow key, store
        # a movement event in the BeeBot.
        if event.key == pygame.K_UP:
            self.store_movement('Forward')

        if event.key == pygame.K_DOWN:
            self.store_movement('Down')

        if event.key == pygame.K_LEFT:
            self.store_movement('Left')

        if event.key == pygame.K_RIGHT:
            self.store_movement('Right')
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
