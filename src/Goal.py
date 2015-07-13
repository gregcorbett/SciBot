import pygame

class Goal(pygame.sprite.Sprite):
	def __init__(self,fileName,startLogicalPositionX,startLogicalPositionY,step):
		
		self.logicalPositionX = startLogicalPositionX
		self.logicalPositionY = startLogicalPositionY
		
		self.screenLocationX = startLogicalPositionX * step
		self.screenLocationY = startLogicalPositionY * step
		
		self.sprite = pygame.image.load(fileName)

	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))