import pygame

class BeeBot(pygame.sprite.Sprite):
	def __init__(self,startLogicalPositionX,startLogicalPositionY,boardHeight,boardWidth,boardStep):
		
		self.logicalPositionX = startLogicalPositionX
		self.logicalPositionY = startLogicalPositionY
		
		self.screenLocationX = startLogicalPositionX * boardStep
		self.screenLocationY = (boardHeight - startLogicalPositionY - 1) * boardStep
		
		self.sprite=pygame.image.load("./img/robot.jpg")
	
	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))
		pygame.display.update()
		
