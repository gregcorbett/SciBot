import pygame
import time

from src.BeeBot import *
from src.Board import *

class GameWindow:
	def __init__(self,logicalHeight,logicalWidth):
		self.step = 150
		
		self.height = logicalHeight*self.step
		self.width = logicalWidth*self.step
		
		self.board = Board(logicalHeight,logicalWidth,self.step)
		self.size = (self.width,self.height)
		
		self.robot = BeeBot(6,3,self.board,Heading.NORTH)
		pygame.init()
		self.screen = pygame.display.set_mode(self.size) 
		
		self.board.display(self.screen)
		self.robot.display(self.screen)
		
	def startInstance(self):
		self.newGame()
	
	def newGame(self):
		self.robot.move(self.screen)
