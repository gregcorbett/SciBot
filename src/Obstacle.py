import pygame

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,fileName,startLogicalPositionY,startLogicalPositionX,board):
		self.board = board
		
		self.logicalPositionX = startLogicalPositionX
		self.logicalPositionY = startLogicalPositionY
		
		self.screenLocationX = startLogicalPositionX * self.board.step
		self.screenLocationY = (board.logicalHeight - startLogicalPositionY - 1) * self.board.step
		
		self.sprite = pygame.image.load(fileName)
		
	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))