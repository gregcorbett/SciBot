import pickle
import pygame

class Scenario:
	def __init__(self,name):
		self.name = name
		self.background = None
		
	def formatImageForPickle(self,input):
		return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"};
		
	def setBackground(self,input):
		self.background = self.formatImageForPickle(input)
		
	def getBackground(self):
		return pygame.image.fromstring(self.background['image'],self.background['size'],self.background['format'])
		
	def writeToFile(self):
		pickle.dump( self, open( "./scenarios/"+ self.name +".scibot", "wb" ) )