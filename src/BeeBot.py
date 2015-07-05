import pygame
import time
from enum import Enum
from enum import IntEnum
import sys

class Heading(Enum):
	NORTH = 1
	EAST = 2
	SOUTH = 3
	WEST = 4

class Direction(IntEnum):
	UP = 1
	LEFT = 2
	DOWN = 3
	RIGHT = 4
	
class BeeBot(pygame.sprite.Sprite):
	def __init__(self,startLogicalPositionY,startLogicalPositionX,board,heading):
		self.board = board
		
		self.logicalPositionX = startLogicalPositionX
		self.logicalPositionY = startLogicalPositionY
		
		self.screenLocationX = startLogicalPositionX * self.board.step
		self.screenLocationY = (board.logicalHeight - startLogicalPositionY - 1) * self.board.step
		
		self.sprites = {}
		
		self.sprites[Heading.NORTH]=pygame.image.load("./img/robot.jpg")
		self.sprites[Heading.EAST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 270)
		self.sprites[Heading.SOUTH]=pygame.transform.rotate(self.sprites[Heading.NORTH], 180)
		self.sprites[Heading.WEST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 90)
		
		self.heading = heading
		
		self.sprite = self.sprites[self.heading]
		
		self.memory = {}
		self.memoryCount = 0
		
	def move(self,event,screen):
		if event.type == pygame.USEREVENT+Direction.UP:
			self.moveForward(screen)
		if event.type == pygame.USEREVENT+Direction.DOWN:
			self.moveBackward(screen)
		if event.type == pygame.USEREVENT+Direction.LEFT:
			self.moveLeft(screen)
		if event.type == pygame.USEREVENT+Direction.RIGHT:
			self.moveRight(screen)	
	
	def addToMemory(self,event):
		self.memory[self.memoryCount] = event
		self.memoryCount = self.memoryCount + 1
		
	def pushOutMemory(self):
		memPtr = 0
		while ( memPtr < self.memoryCount ):
			pygame.event.post(self.memory[memPtr])
			memPtr = memPtr + 1
			time.sleep(0.005)
		self.memory = {}
		self.memoryCount = 0

	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))
	
	def moveBackward(self,screen):
		if (self.heading == Heading.SOUTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
			self.logicalPositionY = self.logicalPositionY + 1
		elif (self.heading == Heading.WEST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX + 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()	
			self.logicalPositionX = self.logicalPositionX + 1
		elif (self.heading == Heading.NORTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY + 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()	
			self.logicalPositionY = self.logicalPositionY - 1
		elif (self.heading == Heading.EAST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
			self.logicalPositionX = self.logicalPositionX - 1
		
		self.checkLocationLogicalConsistent()
		
	def moveForward(self,screen):
		if (self.heading == Heading.NORTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()				
			self.logicalPositionY = self.logicalPositionY + 1
		elif (self.heading == Heading.EAST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX + 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
			self.logicalPositionX = self.logicalPositionX + 1
		elif (self.heading == Heading.SOUTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY + 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
			self.logicalPositionY = self.logicalPositionY - 1
		elif (self.heading == Heading.WEST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
			self.logicalPositionX = self.logicalPositionX - 1
		
		self.checkLocationLogicalConsistent()

	def moveRight(self,screen):
		time.sleep(1)
		self.rotateSprite(-45)
		self.display(screen)
		pygame.display.update()	
		time.sleep(1)
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

	def moveLeft(self,screen):
		time.sleep(1)
		self.rotateSprite(45)
		self.display(screen)
		pygame.display.update()	
		time.sleep(1)
		
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
				
	def rotateSprite(self,angle):
		orig_rect = self.sprite.get_rect()
		rot_image = pygame.transform.rotate(self.sprite, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		self.sprite = rot_image.subsurface(rot_rect).copy()
	
	def checkLocationLogicalConsistent(self):
		if ( self.screenLocationX != self.logicalPositionX * self.board.step):
			print("Error 5: screenLocationX != logicalPositionX")
			print("screenLocationX = ",self.screenLocationX)
			print("logicalPositionX = ",self.logicalPositionX)
			sys.exit()
		if ( ( self.board.logicalHeight - ( self.screenLocationY / self.board.step ) - 1 ) != self.logicalPositionY ): 
			print("Error 6: self.screenLocationY / self.board.step + self.board.logicalHeight - 1 != self.logicalPositionY")
			print("screenLocationY = ",self.screenLocationY)
			print("logicalPositionY",self.logicalPositionY)
			sys.exit()			