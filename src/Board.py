import pygame
import sys
#import time

from src.Obstacle import *
from src.ObstacleGroup import *
from src.Goal import *
from src.GoalGroup import *


class Board:
	def __init__(self,width,height,step,scenario):
		self.step = step
		
		self.logicalHeight = height
		self.logicalWidth = width
		
		self.height = height*step
		self.width = width*step
		
		self.background=scenario.get_element('Background')
		
		self.borderColour = scenario.get_element('BorderColour')
		
		self.obstacleGroup = scenario.get_element('ObstacleGroup')

		self.goalGroup = scenario.get_element('GoalGroup')
		
		if (self.height != self.background.get_height()):
			print("Error 1: board height does not match image height")
			print("Board Height = ",self.height)
			print("Image Height = ",self.background.get_height())
			sys.exit()
		if (self.height != self.background.get_height()):
			print("Error 2: board width does not match image width")
			print("Board Width = ",self.width)
			print("Image Width = ",self.background.get_width())
			sys.exit()
		if ((self.height % self.step) != 0):
			print("Error 3: height % step != 0")
			print("Height = ",self.height)
			print("Step   = ",self.step)
			sys.exit()
		if ((self.width % self.step) != 0):
			print("Error 4: width % step != 0")
			print("Width = ",self.width)
			print("Step  = ",self.step)
			sys.exit()
		
	def display(self,screen):
		screen.blit(self.background,(0,0))
		obsPtr = 0
		while obsPtr < self.obstacleGroup.obstacleCount:
			obs = self.obstacleGroup.obstacles[obsPtr]
			obs.display(screen)
			obsPtr = obsPtr + 1
		self.goalGroup.display(screen)
		
		if self.borderColour != None:
			iterWidth = 0
			while (iterWidth <= self.width):
				pygame.draw.line(screen,self.borderColour,(iterWidth,0),(iterWidth,self.height),5)
				iterWidth = iterWidth + self.step
			
			iterHeight = 0
			while (iterHeight <= self.height):
				pygame.draw.line(screen,self.borderColour,(0,iterHeight),(self.width,iterHeight),5)
				iterHeight = iterHeight + self.step
		
