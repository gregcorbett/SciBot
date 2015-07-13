import pickle
import pygame

class Scenario:
	def __init__(self,name):
		self.name = name
		
		self.boardStep = 0
		self.logicalWidth = 0
		self.logicalHeight = 0
		
		self.background = None
		self.borderColour = None
		
		self.beeBotStartPosition = None
		self.beeBotSprite = None
		self.beeBotHeading = None
		
		self.obstacleGroup = None

	def setObstacleGroup(self,obstacleGroup):
		self.obstacleGroup = obstacleGroup
		for obs in self.obstacleGroup:
			obs.sprite = formatSurfaceForPickle(obs.sprite)
		
	def getObstacleGroup(self):
		for obs in self.obstacleGroup:
			obs.sprite = formatPickleToSurface(obs.sprite)
		return self.obstacleGroup
		
	def setBeeBotHeading(self,input):
		self.beeBotHeading = input

	def getBeeBotHeading(self):
		return self.beeBotHeading
		
	def setBeeBotSprite(self,inputString):
		input = pygame.image.load(inputString)
		self.beeBotSprite = self.formatSurfaceForPickle(input)
		
	def getBeeBotSprite(self):
		return self.formatPickleToSurface(self.beeBotSprite)
		
	def getBeeBotStartPosition(self):
		return self.beeBotStartPosition
		
	def setBeeBotStartPosition(self,input):
		self.beeBotStartPosition = input
	
	def getLogicalHeight(self):
		return self.logicalHeight
		
	def getLogicalWidth(self):
		return self.logicalWidth	

	def setLogicalHeight(self,input):
		self.logicalHeight = input
		
	def setLogicalWidth(self,input):
		self.logicalWidth = input
		
	def getBoardStep(self):
		return self.boardStep
		
	def setBoardStep(self,input):
		self.boardStep = input
	
	def formatPickleToSurface(self,input):
		return pygame.image.fromstring(input['image'],input['size'],input['format'])
	
	def formatSurfaceForPickle(self,input):
		return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"};
		
	def setBackground(self,inputString):
		input = pygame.image.load(inputString)
		self.background = self.formatSurfaceForPickle(input)
		
	def getBackground(self):
		return self.formatPickleToSurface(self.background)
		
	def setBorderColour(self,input):
		self.boardColour = input
	
	def getBorderColour(self):
		return self.boardColour
	
	def writeToFile(self):
		pickle.dump( self, open( "./scenarios/"+ self.name +".scibot", "wb" ) )