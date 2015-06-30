import pygame

class Board:
	def __init__(self,height,width,step):
		self.height = height*step
		self.width = width*step
		self.background=pygame.image.load("./img/background.jpg") 
		
	def display(self,screen):
		screen.blit(self.background,(75,75))
		pygame.display.flip()