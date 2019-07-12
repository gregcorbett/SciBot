"""This file defines the main GameWindow and the Enum RenderingMode."""


from threading import Thread
from pickle import load
from time import sleep
from enum import Enum
import glob
import math
import os
import sys
import pygame
from src.BeeBot import BeeBot
from src.Board import Board
from src.Button import Button
from src.ButtonGroup import ButtonGroup
from src.CommandLog import CommandLog
from src.CustomEvent import CustomEvent
from src.Point import Point
from src.Scenario import Scenario
from src import __version__


class RenderingMode(Enum):
    """A class of Enums determining how the GameWindow will render."""

    TITLE_SCREEN = 1
    CHOOSE_SCENARIO = 2
    LOAD_SCENARIO = 3
    NORMAL = 4
    WIN_SCREEN = 5
    FAIL_SCREEN = 6
    END_RENDERING = 7


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
        # Controls what to render
        self.rendering_mode = None

        # The unpickled Scenario
        self.scenario = None

        # Board Dimensions
        self.step = None
        self.height = None
        self.width = None

        # Variable that holds the Board
        self.board = None
        # Board Dimensions
        self.size = None

        # Variable that holds the BeeBot
        self.robot = None

        # Variable that holds the screen that is draw on
        self.screen = None

        # Used to monitor the frame rate
        self.clock = None

        # The font of the text displayed (excluding buttons)
        self.font = None

        # All Buttons to display
        self.buttons = ButtonGroup()

        # Create an empty CommandLog
        self.command_log = None

        # The logo to display on screen
        self.logo = None

        # If true, the main game loop will be running
        self._logic_running = None
        # If true, the renderer will be running
        self._rendering_running = None

        # Call the superclass constructor
        Thread.__init__(self)

    def start_rendering(self):
        """Change rendering_mode to TITLE_SCREEN and begin rendering."""
        self._rendering_running = True
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.rendering_mode = RenderingMode.TITLE_SCREEN
        self.start()  # Runs the run method.

    def run(self):
        """Run the rendering engine."""
        while self._rendering_running:
            if self.rendering_mode is RenderingMode.TITLE_SCREEN:
                # For now, we will let runSciBot drive the rendering
                pass

            elif self.rendering_mode is RenderingMode.CHOOSE_SCENARIO:
                # Display the background
                self.screen.fill(GameWindow.GREY)

                # Display the Scenario Buttons
                self.buttons.display(self.screen)

                # Update display
                pygame.display.update()

            elif self.rendering_mode is RenderingMode.LOAD_SCENARIO:
                pass  # Maybe one day we'll have a fancy loading bar

            elif self.rendering_mode is RenderingMode.NORMAL:
                self.screen.fill(GameWindow.GREY)

                # Display the Board and BeeBot
                self.board.display(self.screen)
                self.robot.display(self.screen)

                # Display the logo (if any)
                if self.logo is not None:
                    self.screen.blit(self.logo,
                                     Point(self.width + 69, self.height - 85))

                # Display any Buttons
                self.buttons.display(self.screen)

                # Update and refresh the CommandLog
                self.command_log.update(self.robot.memory)
                self.command_log.display(self.screen)

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
                # Let the renderer die
                self._rendering_running = False

    def choose_scenario(self):
        """Choose a Scenario (possibly using a PyGame UI)."""
        # Get the available Scenarios (those under ./scenarios/)
        scenario_list = glob.glob("./scenarios/*.scibot")

        # If no scenarios, exit!
        if len(scenario_list) is 0:
            print("No scibot files found.")
            print("Please place them in ./scenarios/")
            self.rendering_mode = RenderingMode.END_RENDERING
            sleep(1)
            pygame.quit()
            sys.exit()

        # If only one scenario, use that one!
        if len(scenario_list) is 1:
            self.scenario = scenario_list[0]
            return

        # else, Remove Default.scenario from returned list if there
        scenario_list = [scenario for scenario in scenario_list if "Default.scibot" not in scenario]

        # If now only one scenario, use that one!
        if len(scenario_list) is 1:
            self.scenario = scenario_list[0]
            return

        # Determine the size of the window needed to display all the buttons.
        # Set maximum scenarios to display on a single row.
        max_width = 3
        # If scenarios less than max_width, they can be displayed on one row.
        if len(scenario_list) <= max_width:
            height = 1
            width = len(scenario_list)
        else:  # Work out how many rows are needed.
            height = math.ceil(len(scenario_list) / 3.0)
            width = max_width

        # Work out screen size to display 120x120
        # buttons with 10 space between.
        screen_width = 10 + (width * (120 + 10))
        screen_height = 10 + (height * (120 + 10))

        # Variables used to draw Buttons
        # Start a 10 because of padding
        width_counter = 10
        height_counter = 10

        # Empty ButtonGroup
        self.buttons.removal_all()

        for scenario_path in scenario_list:
            # Get the Scenario filename from the full path
            scenario_file = os.path.basename(scenario_path)
            # Add the Scenario filename (minus extension) to a list
            temp = Button(os.path.splitext(scenario_file)[0],
                          GameWindow.BLACK,
                          GameWindow.WHITE,
                          Point(width_counter, height_counter),
                          (120, 120))

            # Add temp Button to ButtonGroup
            self.buttons.add(temp)

            # If the next Button would be printed off screen,
            # start a new row.
            if width_counter > ((width - 1) * 120):
                width_counter = 10
                height_counter = height_counter + 120 + 10
            else:
                width_counter = width_counter + 120 + 10

        # Display the PyGame UI
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.rendering_mode = RenderingMode.CHOOSE_SCENARIO

        # User choose's a Scenario
        while self.scenario is None:
            event = pygame.event.poll()
            # If the event is a left mouse button up
            # assume it is a button press
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # If it was indeed a Button release
                button = self.buttons.get_pressed_button(event.pos)
                if button is not None and button.swapped:
                    # Get the file corresponding to the Button pressed
                    button.swap_colours()
                    self.scenario = "./scenarios/" + button.text + ".scibot"
                else:
                    # Reset all Buttons without doing anything else
                    self.buttons.unswap_all()

            # If the event is a left mouse button up
            # assume it is a button press
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # If it was indeed a Button press
                button = self.buttons.get_pressed_button(event.pos)
                if button is not None:
                    # Mark that Button as being pressed
                    button.swap_colours()

            if event.type == pygame.QUIT:
                self.rendering_mode = RenderingMode.END_RENDERING
                sleep(1)
                pygame.quit()
                sys.exit()

    def load_scenario(self):
        """Load the chosen Scenario."""
        self.rendering_mode = RenderingMode.LOAD_SCENARIO
        # Unpickle the Scenario file
        self.scenario = load(open(self.scenario, "rb"))

        # Log Version of the scenario and code
        print("Loading Scenario Version %s with code base Version %s" %
              (self.scenario.get_version(),
               __version__))

        license = self.scenario.get_license()
        if license is not None:
            print("Scenario licensed as follows:")
            print("")
            print(license)
        else:
            print("No license provided in scenario file.")

        # Get the logo to display (if any)
        self.logo = self.scenario.get_logo()

        # Load variables into memory
        self.step = self.scenario.get_board_step()
        self.height = self.scenario.get_logical_height() * self.step
        self.width = self.scenario.get_logical_width() * self.step

        self.board = Board(self.scenario)

        self.robot = BeeBot(self.scenario)

        self.clock = pygame.time.Clock()

        buttons_on_the_left = True

        self.create_buttons(buttons_on_the_left)

        if buttons_on_the_left:
            # Make space for:
            # - the Buttons to the right of the map.
            # - the CommandLog below the map.
            self.size = (self.width + 400, self.height + 30)
            # Create the empty CommandLog
            self.command_log = CommandLog(Point(0, self.height),
                                          (self.width, 30))
        else:
            # Make space for:
            # - the Buttons below the map.
            # - the CommandLog to the right of the map.
            self.size = (self.width + 30, self.height + 400)
            # Create the empty CommandLog
            self.command_log = CommandLog(Point(self.width, 0),
                                          (30, self.height))

        # Only want to do this once, so sadly can't do it in the rendering
        # loop without a potential race condition as
        # size gets set by loading the Scenario
        if self._rendering_running:
            self.screen = pygame.display.set_mode(self.size)

    def create_buttons(self, buttons_on_the_left):
        """Helper method to populate ButtonGroup."""
        # Empty ButtonGroup
        self.buttons.removal_all()

        if buttons_on_the_left:
            forward_button = Button('Forward',
                                    GameWindow.BLACK,
                                    GameWindow.WHITE,
                                    Point(self.width + 140,
                                          float(self.height)/2 - 240),
                                    (120, 120))

            self.buttons.add(forward_button)

            backward_button = Button('Backward',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     Point(self.width + 140,
                                           float(self.height)/2 + 20),
                                     (120, 120))

            self.buttons.add(backward_button)

            turn_left_button = Button('Turn Left',
                                      GameWindow.BLACK,
                                      GameWindow.WHITE,
                                      Point(self.width + 10,
                                            float(self.height)/2 - 110),
                                      (120, 120))

            self.buttons.add(turn_left_button)

            turn_right_button = Button('Turn Right',
                                       GameWindow.BLACK,
                                       GameWindow.WHITE,
                                       Point(self.width + 270,
                                             float(self.height)/2 - 110),
                                       (120, 120))

            self.buttons.add(turn_right_button)

            go_button = Button('Go',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               Point(self.width + 140,
                                     float(self.height)/2 - 110),
                               (120, 120))

            self.buttons.add(go_button)

            stop_button = Button('Stop',
                                 GameWindow.WHITE,
                                 GameWindow.RED,
                                 Point(self.width + 140,
                                       float(self.height)/2 - 110),
                                 (120, 120),
                                 False)

            self.buttons.add(stop_button)

            reset_button = Button('Reset',
                                  GameWindow.BLACK,
                                  GameWindow.WHITE,
                                  Point(self.width + 10,
                                        float(self.height)/2 + 20),
                                  (120, 120))

            self.buttons.add(reset_button)

            clear_button = Button('Clear',
                                  GameWindow.BLACK,
                                  GameWindow.WHITE,
                                  Point(self.width + 270,
                                        float(self.height)/2 + 20),
                                  (120, 120))

            self.buttons.add(clear_button)

        else:
            forward_button = Button('Forward',
                                    GameWindow.BLACK,
                                    GameWindow.WHITE,
                                    Point(float(self.width)/2 - 60,
                                          self.height + 10),
                                    (120, 120))

            self.buttons.add(forward_button)

            backward_button = Button('Backward',
                                     GameWindow.BLACK,
                                     GameWindow.WHITE,
                                     Point(float(self.width)/2 - 60,
                                           self.height + 270),
                                     (120, 120))

            self.buttons.add(backward_button)

            turn_left_button = Button('Turn Left',
                                      GameWindow.BLACK,
                                      GameWindow.WHITE,
                                      Point(float(self.width)/2 - 190,
                                            self.height + 140),
                                      (120, 120))

            self.buttons.add(turn_left_button)

            turn_right_button = Button('Turn Right',
                                       GameWindow.BLACK,
                                       GameWindow.WHITE,
                                       Point(float(self.width)/2 + 70,
                                             self.height + 140),
                                       (120, 120))

            self.buttons.add(turn_right_button)

            go_button = Button('Go',
                               GameWindow.BLACK,
                               GameWindow.WHITE,
                               Point(float(self.width)/2 - 60,
                                     self.height + 140),
                               (120, 120))

            self.buttons.add(go_button)

            stop_button = Button('Stop',
                                 GameWindow.WHITE,
                                 GameWindow.RED,
                                 Point(float(self.width)/2 - 60,
                                       self.height + 140),
                                 (120, 120),
                                 False)

            self.buttons.add(stop_button)

            reset_button = Button('Reset',
                                  GameWindow.BLACK,
                                  GameWindow.WHITE,
                                  Point(float(self.width)/2 - 190,
                                        self.height + 270),
                                  (120, 120))

            self.buttons.add(reset_button)

            clear_button = Button('Clear',
                                  GameWindow.BLACK,
                                  GameWindow.WHITE,
                                  Point(float(self.width)/2 + 70,
                                        self.height + 270),
                                  (120, 120))

            self.buttons.add(clear_button)

    def start_logic(self, scenario=None):
        """
        Start the game logic.

        Possibly using some settings passed as arguments.
        """
        self._logic_running = True
        # If we don't pass a scenario as an argument
        if scenario is None:
            # Choose Scenario
            self.choose_scenario()
        else:
            # Otherwise, use the one passed as an argument
            self.scenario = 'scenarios/%s.scibot' % scenario

        # Load the chosen scenario
        try:
            self.load_scenario()
        except ValueError as error:
            print(error)
            self.rendering_mode = RenderingMode.END_RENDERING
            pygame.quit()
            sys.exit()

        # Go to NORMAL rendering
        self.rendering_mode = RenderingMode.NORMAL
        while self._logic_running:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                self.rendering_mode = RenderingMode.END_RENDERING
                sleep(1)
                pygame.quit()
                sys.exit()

            elif event.type == CustomEvent.RUN_FAIL:
                self.robot.crash()
                sleep(1)
                self.rendering_mode = RenderingMode.FAIL_SCREEN
                sleep(2)
                self.rendering_mode = RenderingMode.NORMAL
                self.stop_beebot_movement()
                self.robot.reset_position()
                self.robot.clear_memory()
                self.board.goal_group.reset_all_goals()

            elif event.type == CustomEvent.RUN_WIN:
                sleep(1)
                self.rendering_mode = RenderingMode.WIN_SCREEN
                sleep(2)
                self.rendering_mode = RenderingMode.END_RENDERING
                sleep(1)
                pygame.quit()
                # End the loop
                self._logic_running = False

            # If the event is a left mouse button up
            # assume it is a button press
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button = self.buttons.get_pressed_button(event.pos)
                if button is not None and button.swapped:
                    button.swap_colours()
                    self.handle_button_press(button)
                else:
                    self.buttons.unswap_all()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                button = self.buttons.get_pressed_button(event.pos)
                if button is not None:
                    button.swap_colours()

            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event)

            # If the event is a movement event
            # Move the BeeBot.
            elif (event.type >= CustomEvent.MOVE_BEEBOT_UP and
                  event.type <= CustomEvent.MOVE_BEEBOT_RIGHT):

                self.robot.move(event)
                self.check_for_obstacle_collisions()
                self.check_for_goal_collisions()
                self.check_for_off_map()

            elif self.robot.running:
                # If there are no further instructions in the BeeBot's memory
                if len(self.robot.memory) == self.robot.index:
                    # Stop the BeeBot
                    self.stop_beebot_movement()
                else:
                    # Push out the next instruction
                    self.robot.push_out_memory()

        # If we get here, the main game loop has exited sommehow
        # Let's exit safely
        self.rendering_mode = RenderingMode.END_RENDERING
        sleep(1)
        pygame.quit()
        # No need to sys.exit() here as this is the end of the loop

    def check_for_goal_collisions(self):
        """Check if the BeeBot is currently on a Goal."""
        # If so, mark that Goal as met.
        # If all Goals met, push a CustomEvent.RUN_WIN.
        if self.board.goal_group.is_ordered:
            goal = self.board.goal_group.get_current_goal()
            if self.robot.logical_position.is_equal_to(goal.logical_position):
                goal.complete()
                if goal.should_increment_beebot_sprite:
                    self.robot.increment_sprite()
                self.board.goal_group.increment_pointer()

        else:
            for goal in self.board.goal_group.components:
                if self.robot.logical_position.is_equal_to(goal.logical_position):
                    goal.complete()
                    if goal.should_increment_beebot_sprite:
                        self.robot.increment_sprite()

        if self.board.goal_group.have_all_goals_been_met():
            # clear any remaining events
            pygame.event.clear()
            # push a win event
            pygame.event.post(pygame.event.Event(CustomEvent.RUN_WIN))

    def start_beebot_movement(self):
        """Start the BeeBot moving and turn the Go Buton to the Stop Button."""
        if not self.robot.running:
            self.robot.running = True

            self.buttons.get_named_button('Go').displayed = False
            self.buttons.get_named_button('Stop').displayed = True

            # Hide 'Reset' and 'Clear' Buttons to prevent them
            # being pressed mid run as this can cause odd
            # behaviour where a reset BeeBot continues to movement
            # or a running BeeBot has no instructions to run.
            self.buttons.get_named_button('Reset').displayed = False
            self.buttons.get_named_button('Clear').displayed = False

            # Prevent the BeeBot being 'programmed' while running
            self.buttons.get_named_button('Forward').displayed = False
            self.buttons.get_named_button('Turn Left').displayed = False
            self.buttons.get_named_button('Backward').displayed = False
            self.buttons.get_named_button('Turn Right').displayed = False

    def stop_beebot_movement(self):
        """Stop the BeeBot moving and turn the Stop Buton to the Go Button."""
        if self.robot.running:
            self.robot.running = False
            # Reset the BeeBot memory pointer to the start of the instructions
            self.robot.index = 0

            # Clear the queue incase movement events have already
            # been pushed to the queue.
            pygame.event.clear()

            self.buttons.get_named_button('Go').displayed = True
            self.buttons.get_named_button('Stop').displayed = False

            # Now that movement has stopped, these Buttons cannot cause
            # odd side effects any more, so display them once again.
            self.buttons.get_named_button('Reset').displayed = True
            self.buttons.get_named_button('Clear').displayed = True

            # Allow the BeeBot to be programmed again.
            self.buttons.get_named_button('Forward').displayed = True
            self.buttons.get_named_button('Turn Left').displayed = True
            self.buttons.get_named_button('Backward').displayed = True
            self.buttons.get_named_button('Turn Right').displayed = True

    def fail_run(self):
        """Clear the event queue and push a RUN_FAIL event."""
        # clear any remaining events
        pygame.event.clear()
        # push a fail event
        pygame.event.post(pygame.event.Event(CustomEvent.RUN_FAIL))

    def check_for_obstacle_collisions(self):
        """Check if the BeeBot is currently on a Obstacle."""
        # If so, push a CustomEvent.RUN_FAIL.
        for obstacle in self.board.obstacle_group.components:
            if self.robot.logical_position.is_equal_to(obstacle.logical_position):
                self.fail_run()

    def check_for_off_map(self):
        """Check if the BeeBot is off the map."""
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
            # Push a MOVE_BEEBOT_UP event
            new_event = CustomEvent.MOVE_BEEBOT_UP
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Left':
            # Push a MOVE_BEEBOT_LEFT event
            new_event = CustomEvent.MOVE_BEEBOT_LEFT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Right':
            # Push a MOVE_BEEBOT_RIGHT event
            new_event = CustomEvent.MOVE_BEEBOT_RIGHT
            self.robot.add_to_memory(pygame.event.Event(new_event))

        if movement == 'Backward':
            # Push a MOVE_BEEBOT_DOWN event
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
            # Reset the BeeBots position and the completed status of the Goals.
            self.robot.reset_position()
            self.board.goal_group.reset_all_goals()

        if button.text == 'Clear':
            # Remove any stored instructions
            self.robot.memory = []

        if button.text == 'Go':
            self.start_beebot_movement()

        if button.text == 'Stop':
            self.stop_beebot_movement()

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
        # reset the BeeBot's position and clears any completed Goals.
        # it doesn't clear the memory!
        if event.key == pygame.K_SPACE:
            self.robot.reset_position()
            self.board.goal_group.reset_all_goals()

        # if the event is the X key, clear the BeeBot's memory
        if event.key == ord('x') or event.key == ord('X'):
            self.robot.memory = []

        # if the event is the G key, start the BeeBot.
        if event.key == ord('g') or event.key == ord('G'):
            self.start_beebot_movement()

        # if the event is the S key, stop the BeeBot.
        if event.key == ord('s') or event.key == ord('S'):
            self.stop_beebot_movement()
