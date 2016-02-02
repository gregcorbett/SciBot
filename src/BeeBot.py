"""This file defines the BeeBot class and the Heading Enum."""


from enum import Enum
#from time import sleep
from src.CustomEvent import CustomEvent
import pygame
import time

class Heading(Enum):
    """This class defines Enums for the heading of a BeeBot."""

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class BeeBot(pygame.sprite.Sprite):
    """This class defines the BeeBot."""

    def __init__(self, board, scenario):
        """Create a BeeBot."""
        self.board = board  # TODO: why is this needed?

        start_logical_position_x, start_logical_position_y = scenario.get_element('BeeBotStartPosition')

        self.screen_location_x = start_logical_position_x * self.board.step
        self.screen_location_y = start_logical_position_y * self.board.step

        self.logical_position_x = start_logical_position_x
        self.logical_position_y = start_logical_position_y

        self.sprites = {}

        self.sprites[Heading.NORTH]=scenario.get_element('BeeBotSprite')

        self.sprites[Heading.EAST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 270)
        self.sprites[Heading.SOUTH]=pygame.transform.rotate(self.sprites[Heading.NORTH], 180)
        self.sprites[Heading.WEST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 90)

        self.heading = scenario.get_element('BeeBotHeading')

        self.sprite = self.sprites[self.heading]

        self.failSprite = scenario.get_element('BeeBotFailSprite')

        self.memory = {}
        self.memoryCount = 0

    def move(self,event,screen):
        if event.type == CustomEvent.MOVE_BEEBOT_UP:
            self.moveForward(screen)
            time.sleep(0.5)
        if event.type == CustomEvent.MOVE_BEEBOT_DOWN:
            self.moveBackward(screen)
            time.sleep(0.5)
        if event.type == CustomEvent.MOVE_BEEBOT_LEFT:
            self.moveLeft(screen)
            time.sleep(0.5)
        if event.type == CustomEvent.MOVE_BEEBOT_RIGHT:
            self.moveRight(screen)
            time.sleep(0.5)

    def addToMemory(self,event):
        self.memory[self.memoryCount] = event
        self.memoryCount = self.memoryCount + 1

    def pushOutMemory(self):
        memPtr = 0
        while ( memPtr < self.memoryCount ):
            pygame.event.post(self.memory[memPtr])
            memPtr = memPtr + 1

    def clearMemory(self):
        self.memory = {}
        self.memoryCount = 0

    def resetMemory(self):
        self.memory = safe.safeMem
        self.memoryCount = safe.safeMemCount

    def display(self,screen):
        screen.blit(self.sprite,(self.screen_location_x,self.screen_location_y))

    def moveBackward(self,screen):
        if (self.heading == Heading.SOUTH ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_y = self.screen_location_y - 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_y = self.logical_position_y - 1
        elif (self.heading == Heading.WEST ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_x = self.screen_location_x + 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_x = self.logical_position_x + 1
        elif (self.heading == Heading.NORTH ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_y = self.screen_location_y + 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_y = self.logical_position_y + 1
        elif (self.heading == Heading.EAST ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_x = self.screen_location_x - 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_x = self.logical_position_x - 1

        self.checkLocationLogicalConsistent()

    def moveForward(self,screen):
        if (self.heading == Heading.NORTH ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_y = self.screen_location_y - 1
                time.sleep(0.01)
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_y = self.logical_position_y - 1
        elif (self.heading == Heading.EAST ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_x = self.screen_location_x + 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_x = self.logical_position_x + 1
        elif (self.heading == Heading.SOUTH ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_y = self.screen_location_y + 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_y = self.logical_position_y + 1
        elif (self.heading == Heading.WEST ):
            incrStep = 0
            while ( incrStep < self.board.step ):
                incrStep = incrStep + 1
                self.screen_location_x = self.screen_location_x - 1
                #self.board.display(screen)
                #self.display(screen)
                #pygame.display.update()
            self.logical_position_x = self.logical_position_x - 1

        self.checkLocationLogicalConsistent()

    def moveRight(self,screen):
        time.sleep(0.5)
        self.rotateSprite(-45)
        #self.board.display(screen)
        #self.display(screen)
        #pygame.display.update()
        time.sleep(0.5)
        if (self.heading == Heading.NORTH ):
            self.heading = Heading.EAST
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.EAST ):
            self.heading = Heading.SOUTH
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.SOUTH ):
            self.heading = Heading.WEST
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.WEST ):
            self.heading = Heading.NORTH
            self.sprite = self.sprites[self.heading]

        time.sleep(0.5)

    def moveLeft(self,screen):
        time.sleep(0.5)
        self.rotateSprite(45)
        #self.board.display(screen)
        #self.display(screen)
        #pygame.display.update()
        time.sleep(0.5)

        if (self.heading == Heading.NORTH ):
            self.heading = Heading.WEST
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.EAST ):
            self.heading = Heading.NORTH
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.SOUTH ):
            self.heading = Heading.EAST
            self.sprite = self.sprites[self.heading]
        elif (self.heading == Heading.WEST ):
            self.heading = Heading.SOUTH
            self.sprite = self.sprites[self.heading]

        time.sleep(0.5)

    def rotateSprite(self,angle):
        sprite_copy = self.sprite.copy()  # this seems to stop thread errors
        orig_rect = sprite_copy.get_rect()
        rot_image = pygame.transform.rotate(sprite_copy, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        self.sprite = rot_image.subsurface(rot_rect).copy()

    def checkLocationLogicalConsistent(self):
        if ( self.screen_location_x != self.logical_position_x * self.board.step):
            print("Error 5: screen_location_x != logical_position_x")
            print("screen_location_x = ",self.screen_location_x)
            print("logical_position_x = ",self.logical_position_x)
            sys.exit()
        if ( self.screen_location_y != self.logical_position_y * self.board.step):
            print("Error 6: self.screen_location_y / self.board.step + self.board.logicalHeight - 1 != self.logical_position_y")
            print("screen_location_y = ",self.screen_location_y)
            print("logical_position_y",self.logical_position_y)
            sys.exit()
