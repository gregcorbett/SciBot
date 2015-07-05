import pygame
import time
from enum import Enum
from enum import IntEnum

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
		
		self.screenLocationX = startLogicalPositionX * board.step
		self.screenLocationY = (board.logicalHeight - startLogicalPositionY - 1) * board.step
		
		self.sprites = {}
		
		self.sprites[Heading.NORTH]=pygame.image.load("./img/robot.jpg")
		self.sprites[Heading.EAST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 270)
		self.sprites[Heading.SOUTH]=pygame.transform.rotate(self.sprites[Heading.NORTH], 180)
		self.sprites[Heading.WEST]=pygame.transform.rotate(self.sprites[Heading.NORTH], 90)
		
		self.heading = heading
		
		self.sprite = self.sprites[self.heading]
	
	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))
	
	def move(self,screen):
		self.moveForward(screen)
		self.moveBackward(screen)

		self.moveRight(screen)
		self.moveForward(screen)
		self.moveBackward(screen)

		self.moveRight(screen)
		self.moveForward(screen)
		self.moveBackward(screen)

		self.moveRight(screen)
		self.moveForward(screen)
		self.moveBackward(screen)

		self.moveRight(screen)
		self.moveForward(screen)
		self.moveBackward(screen)


	def moveBackward(self,screen):
		if (self.heading == Heading.SOUTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
				self.logicalPositionY = self.logicalPositionY - 1
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
				print(self.screenLocationY)
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY + 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()	
				self.logicalPositionY = self.logicalPositionY + 1
		elif (self.heading == Heading.EAST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
				self.logicalPositionX = self.logicalPositionX - 1
		
	def moveForward(self,screen):
		if (self.heading == Heading.NORTH ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationY = self.screenLocationY - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()				
				self.logicalPositionY = self.logicalPositionY - 1
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
				self.logicalPositionY = self.logicalPositionY + 1
		elif (self.heading == Heading.WEST ):
			incrStep = 0
			while ( incrStep < self.board.step ):
				incrStep = incrStep + 1
				self.screenLocationX = self.screenLocationX - 1
				self.board.display(screen)
				self.display(screen)
				pygame.display.update()		
				self.logicalPositionX = self.logicalPositionX - 1

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

		#if (self.heading == Heading.NORTH ):
		#else if (self.heading == Heading.EAST ):
		#else if (self.heading == Heading.SOUTH ):
		#else if (self.heading == Heading.SOUTH ):
		
		#if (self.heading == Heading.NORTH ):
		#else if (self.heading == Heading.EAST ):
		#else if (self.heading == Heading.SOUTH ):
		#else if (self.heading == Heading.SOUTH ):
		
		#self.rotateSprite(45)
		#self.board.display(screen)
		#self.display(screen)
		
#		incrAngle = 0
#		while ( incrAngle < 90 ):
#			incrAngle = incrAngle + 45
#			self.rotateSprite(45)
#			self.board.display(screen)
#			self.display(screen)
#			time.sleep(1)
#		
#		incrStep = 0
#		while ( incrStep < self.board.step ):
#			incrStep = incrStep + 1
#			self.screenLocationY = self.screenLocationY + 1
#			self.board.display(screen)
#			self.display(screen)
		
#		self.logicalPositionY = self.logicalPositionY + 1	
		
	def rotateSprite(self,angle):
		orig_rect = self.sprite.get_rect()
		rot_image = pygame.transform.rotate(self.sprite, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		self.sprite = rot_image.subsurface(rot_rect).copy()
		#return rot_image