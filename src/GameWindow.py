import pygame
import time
import threading
import pickle

from src.BeeBot import *
from src.Board import *
from src.CustomEvent import *
from src.Scenario import *

from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

class GameWindow():
    def __init__(self):
        pygame.init()
        #basicFont = pygame.font.SysFont("./freesansbold.tff",48)

    def chooseScenario(self):
        self.scenario = None
        #Somehow choose a scenario

        #self.scenario = "UV"

        if self.scenario == None:
            self.scenario = "Default"

        self.scenario = pickle.load( open( "./scenarios/" + self.scenario + ".scibot", "rb" ) )

    def loadScenario(self):

        self.step = self.scenario.get_element('BoardStep')
        self.height = self.scenario.get_element('LogicalHeight')*self.step
        self.width = self.scenario.get_element('LogicalWidth')*self.step

        self.board = Board(self.scenario.get_element('LogicalWidth'),self.scenario.get_element('LogicalHeight'),self.step,self.scenario) #Board.py
        self.size = (self.width,self.height)

        self.robot = BeeBot(self.board,self.scenario)
        safeMem ={}
        safeMemCount = 0

        self.screen = pygame.display.set_mode(self.size)

        self.display()

        self.clock = pygame.time.Clock()

    def startScenario(self):

        while True:
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == CustomEvent.RUN_FAIL:
                time.sleep(2)

                self.screen.fill(BLACK) # displaying a fail message
                basicFont = pygame.font.Font("./src/freesansbold.ttf", 30)
                text = basicFont.render('Oh no, you crashed! Try again!', True, WHITE, BLACK)
                textRect = text.get_rect()
                textRect.centerx = self.screen.get_rect().centerx
                textRect.centery = self.screen.get_rect().centery
                self.screen.blit(text, textRect)
                pygame.display.update()
                time.sleep(2)

                safeMem = self.robot.memory                 # saving moves so far
                safeMemCount = self.robot.memoryCount
                self.robot = BeeBot(self.board,self.scenario)# resetting the board
                self.robot.memory = safeMem                 # resetting memory of moves
                self.robot.memoryCount = safeMemCount
                #pygame.quit()
                #sys.exit()

            if event.type == CustomEvent.RUN_WIN:
                time.sleep(2)

                self.screen.fill(RED) # displaying a win message
                basicFont = pygame.font.Font("./src/freesansbold.ttf", 30)
                text = basicFont.render('Hooray you won!! Play again!', True, WHITE, RED)
                textRect = text.get_rect()
                textRect.centerx = self.screen.get_rect().centerx
                textRect.centery = self.screen.get_rect().centery
                self.screen.blit(text, textRect)
                pygame.display.update()
                time.sleep(2)

                self.board.goalGroup.goalPtr = 0 # resetting the wins
                safeMem = self.robot.memory                 # saving moves so far
                safeMemCount = self.robot.memoryCount
                self.robot = BeeBot(self.board,self.scenario) # resetting the board
                self.robot.memory = safeMem                 # resetting memory of moves
                self.robot.memoryCount = safeMemCount
                #pygame.quit()
                #sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP))
                if event.key == pygame.K_DOWN:
                    self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN))
                if event.key == pygame.K_LEFT:
                    self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT))
                if event.key == pygame.K_RIGHT:
                    self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT))
                if event.key == pygame.K_SPACE: # space puts the robot back to the start - it doesn't clear the memory!
                                        safeMem = self.robot.memory
                                        safeMemCount = self.robot.memoryCount
                                        self.robot = BeeBot(self.board,self.scenario)
                                        self.robot.memory = safeMem
                                        self.robot.memoryCount = safeMemCount
                if event.key == ord('x') or event.key == ord('X'):  # X clears the memory
                                        self.robot.memoryCount = safeMemCount
                if event.key == ord('g') or event.key == ord('G'):
                        self.robot.pushOutMemory()

            if event.type >= CustomEvent.MOVE_BEEBOT_UP and event.type <= CustomEvent.MOVE_BEEBOT_RIGHT:
                self.robot.move(event,self.screen)
                self.checkForObstacleCollisions()
                self.checkForGoalCollisions()

            self.display()
            pygame.display.update()
            self.clock.tick(30)


    def checkForGoalCollisions(self):
        currentGoal = self.board.goalGroup.goals[self.board.goalGroup.goalPtr]
        if self.robot.logical_position_x == currentGoal.logical_position_x and self.robot.logical_position_y == currentGoal.logical_position_y:
            self.board.goalGroup.goalPtr = self.board.goalGroup.goalPtr + 1
            if self.board.goalGroup.goalPtr == self.board.goalGroup.goalCount:
                #final goal
                pygame.event.clear()
                pygame.event.post(pygame.event.Event(CustomEvent.RUN_WIN))

    def checkForObstacleCollisions(self):
        obsPtr = 0
        while obsPtr < self.board.obstacleGroup.obstacleCount:
            obs = self.board.obstacleGroup.obstacles[obsPtr]
            if self.robot.logical_position_x == obs.logical_position_x and self.robot.logical_position_y == obs.logical_position_y:
                self.robot.sprite = self.robot.failSprite
                pygame.event.clear()
                pygame.event.post(pygame.event.Event(CustomEvent.RUN_FAIL))
            obsPtr = obsPtr + 1

    def display(self):
        self.board.display(self.screen)
        self.robot.display(self.screen)
