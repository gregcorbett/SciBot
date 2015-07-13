import pickle
import pygame
from src.Obstacle import *
from src.ObstacleGroup import *
from src.Goal import *
from src.GoalGroup import *

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
		
		self.obstacleGroup = {}
		self.obstacleCount = 0

		self.goalGroup = {}
		self.goalCount = 0
		
		self.beeBotFailSprite = None
	
	def setBeeBotFailSprite(self,inputString):
		input = pygame.image.load(inputString)
		self.beeBotFailSprite = self.formatSurfaceForPickle(input)
		
	def getBeeBotFailSprite(self):
		return self.formatPickleToSurface(self.beeBotFailSprite)
	
	def addGoal(self,sprite,x,y):
		self.goalGroup[self.goalCount] = (sprite,x,y)
		self.goalCount = self.goalCount + 1
		
	def getGoalGroup(self):
		goalGroup = GoalGroup()
		goalPtr = 0
		while goalPtr < self.goalCount:
			pickledGoal = self.goalGroup[goalPtr]
			goalGroup.add(Goal(pygame.image.load(pickledGoal[0]),pickledGoal[1],pickledGoal[2],self.boardStep))
			goalPtr = goalPtr + 1
		self.goalGroup = goalGroup
		return self.goalGroup
	
	def addObstacle(self,sprite,x,y):
		self.obstacleGroup[self.obstacleCount] = (sprite,x,y)
		self.obstacleCount = self.obstacleCount + 1
		
	def getObstacleGroup(self):
		obstacleGroup = ObstacleGroup()
		obsPtr = 0
		while obsPtr < self.obstacleCount:
			pickledObs = self.obstacleGroup[obsPtr]
			obstacleGroup.add(Obstacle(pygame.image.load(pickledObs[0]),pickledObs[1],pickledObs[2],self.boardStep))
			obsPtr = obsPtr + 1
		self.obstacleGroup = obstacleGroup
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
		return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"}
		
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