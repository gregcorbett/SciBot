import pygame
import time

from src.BeeBot import *
from src.Board import *

class GameWindow:
	def __init__(self,height,width):
		self.step = 150
		
		self.height = height*self.step
		self.width = width*self.step
		
		self.board = Board(height,width,self.step)
		self.size = (self.width,self.height)
		
		pygame.init()
		self.screen = pygame.display.set_mode(self.size) 
		
	def newGame(self):
		self.board.display(self.screen)