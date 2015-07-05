import pygame
import time
import threading

from src.BeeBot import *
from src.Board import *

class GameWindow():#threading.Thread):
	def __init__(self,logicalHeight,logicalWidth):
		pygame.init()
	#	super(GameWindow,self).__init__()
		
		self.step = 150
		
		self.height = logicalHeight*self.step
		self.width = logicalWidth*self.step
		
		self.board = Board(logicalHeight,logicalWidth,self.step)
		self.size = (self.width,self.height)
		
		self.robot = BeeBot(6,3,self.board,Heading.NORTH)
		
		self.screen = pygame.display.set_mode(self.size) 
		
		self.board.display(self.screen)
		self.robot.display(self.screen)
		
	def startInstance(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.robot.moveForward(self.screen)
					if event.key == pygame.K_DOWN:
						self.robot.moveBackward(self.screen)
					if event.key == pygame.K_LEFT:
						self.robot.moveLeft(self.screen)
					if event.key == pygame.K_RIGHT:
						self.robot.moveRight(self.screen)
				
			#newEvent = pygame.event.Event(Direction.LEFT)
			#print(newEvent.type)
			#pygame.quit()
			#sys.exit()
			self.display()
			pygame.display.update()
	
	def newGame(self):
		self.robot.move(self.screen)
		
	def display(self):
		self.board.display(self.screen)
		self.robot.display(self.screen)
	
	#def run(self):
	#		clock = pygame.time.Clock()
	#		while True:
	#			self.board.display(self.screen)
	#			self.robot.display(self.screen)
	#			pygame.display.update()
				#time.sleep(0.2)
				#clock.tick(30)