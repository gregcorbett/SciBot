import pygame
import time
from enum import Enum

class Heading(Enum):
	NORTH = 1
	EAST = 2
	SOUTH = 3
	WEST = 4

class BeeBot(pygame.sprite.Sprite):
	def __init__(self,startLogicalPositionY,startLogicalPositionX,board):
		
		self.board = board
		
		self.logicalPositionX = startLogicalPositionX
		self.logicalPositionY = startLogicalPositionY
		
		self.screenLocationX = startLogicalPositionX * board.step
		self.screenLocationY = (board.logicalHeight - startLogicalPositionY - 1) * board.step
		
		self.sprites = {}
		self.sprites[Heading.NORTH]=pygame.image.load("./img/robot.jpg")
		self.heading = Heading.NORTH
		self.sprite = self.sprites[self.heading]
	
	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))
		pygame.display.update()
		
	def move(self,screen):
		##lets move forward/up first
		
		incrStep = 0
		while ( incrStep < self.board.step ):
			incrStep = incrStep + 1
			self.screenLocationY = self.screenLocationY - 1
			self.board.display(screen)
			self.display(screen)
		
		self.logicalPositionY = self.logicalPositionY - 1
		
		#self.rotateSprite(45)
		#self.board.display(screen)
		#self.display(screen)
		
		incrAngle = 0
		while ( incrAngle < 90 ):
			incrAngle = incrAngle + 45
			self.rotateSprite(45)
			self.board.display(screen)
			self.display(screen)
			time.sleep(1)
		
		incrStep = 0
		while ( incrStep < self.board.step ):
			incrStep = incrStep + 1
			self.screenLocationY = self.screenLocationY + 1
			self.board.display(screen)
			self.display(screen)
		
		self.logicalPositionY = self.logicalPositionY + 1
		

		
		
	def rotateSprite(self,angle):
		orig_rect = self.sprite.get_rect()
		rot_image = pygame.transform.rotate(self.sprite, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		self.sprite = rot_image.subsurface(rot_rect).copy()
		#return rot_image