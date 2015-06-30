import pygame

class BeeBot(pygame.sprite.Sprite):
	def __init__(self,startPositionX=0,startPositionY=0):
		self.screenLocationX=startPositionX
		self.screenLocationY=startPositionY
		self.sprite=pygame.image.load("./img/robot.jpg")
	
	def display(self,screen):
		screen.blit(self.sprite,(self.screenLocationX,self.screenLocationY))
		pygame.display.update()
		
