import pygame
import sys

class Board:
	def __init__(self,height,width,step):
		self.height = height*step
		self.width = width*step
		self.background=pygame.image.load("./img/background.jpg")
		self.borderColour = (0,0,255)
		
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
		
	def display(self,screen):
		screen.blit(self.background,(0,0))
		pygame.draw.line(screen,self.borderColour,(60,60),(120,120),4)
		
		pygame.display.update()