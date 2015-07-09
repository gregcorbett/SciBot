import pickle
import pygame

class Scenario:
	def __init__(self,name):
		self.name = name
		self.background = None
		self.borderColour = None
		self.obstacles = None
		
	def formatSurfaceForPickle(self,input):
		return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"};
		
	def setBackground(self,inputString):
		input = pygame.image.load(inputString)
		self.background = self.formatSurfaceForPickle(input)
		
	def getBackground(self):
		return pygame.image.fromstring(self.background['image'],self.background['size'],self.background['format'])
		
	def setBorderColour(self,input):
		self.boardColour = input
	
	def getBorderColour(self):
		return self.boardColour
	
	def writeToFile(self):
		pickle.dump( self, open( "./scenarios/"+ self.name +".scibot", "wb" ) )