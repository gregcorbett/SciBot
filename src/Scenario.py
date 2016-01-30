import pickle
import pygame
from src.Obstacle import *
from src.ObstacleGroup import *
from src.Goal import *
from src.GoalGroup import *

class Scenario():

	def __init__(self,name):
				
		self.elements = {}
		self.name = name
		self.elements['Name'] = name
			
	def get_element(self,key):
	
		if key not in self.elements:
			return None
		
		switcher = {
			'Name': self.getName(),
			'BoardStep': self.getBoardStep(),
			'LogicalWidth': self.getLogicalWidth(),
			'LogicalHeight': self.getLogicalHeight(),
			'Background': self.getBackground(),
			'BorderColour': self.getBorderColour(),
			'BeeBotSprite': self.getBeeBotSprite(),
			'BeeBotStartPosition': self.getBeeBotStartPosition(),
			'BeeBotHeading': self.getBeeBotHeading(),
			'ObstacleGroup': self.getObstacleGroup(),
			'ObstacleCount': self.getObstacleCount(),
			'GoalGroup': self.getGoalGroup(),
			'GoalCount': self.getGoalCount(),
			'BeeBotFailSprite': self.getBeeBotFailSprite(),
		}
		
		return switcher.get(key)
		
	def setBeeBotFailSprite(self,inputString):
		input = pygame.image.load(inputString)
		self.elements['BeeBotFailSprite'] = self.formatSurfaceForPickle(input)
		
	def getBeeBotFailSprite(self):
		return self.formatPickleToSurface(self.elements['BeeBotFailSprite'])
	
	def addGoal(self,x,y,sprite=None):
	
		if 'GoalGroup' not in self.elements:
			self.elements['GoalGroup'] = {}
			self.elements['GoalCount'] = 0
			
		if sprite != None:
			sprite = pygame.image.load(sprite)
			sprite = self.formatSurfaceForPickle(sprite)

		self.elements['GoalGroup'][self.elements['GoalCount']] = (sprite,x,y)
		self.elements['GoalCount'] = self.elements['GoalCount'] + 1
		
	def getGoalGroup(self):
		goalGroup = GoalGroup()
		goalPtr = 0
		while goalPtr < self.elements['GoalCount']:
			pickledGoal = self.elements['GoalGroup'][goalPtr]
			goalGroup.add(Goal(self.formatPickleToSurface(pickledGoal[0]),pickledGoal[1],pickledGoal[2],self.elements['BoardStep']))
			goalPtr = goalPtr + 1
		return goalGroup

	def addObstacle(self,x,y,sprite=None):
	
		if 'ObstacleGroup' not in self.elements:
			self.elements['ObstacleGroup'] = {}
			self.elements['ObstacleCount'] = 0
			
		if sprite != None:
			sprite = pygame.image.load(sprite)
			sprite = self.formatSurfaceForPickle(sprite)
		self.elements['ObstacleGroup'][self.elements['ObstacleCount']] = (sprite,x,y)
		self.elements['ObstacleCount'] = self.elements['ObstacleCount'] + 1
	
	def getObstacleGroup(self):
		obstacleGroup = ObstacleGroup()
		obsPtr = 0
		while obsPtr < self.elements['ObstacleCount']:
			pickledObs = self.elements['ObstacleGroup'][obsPtr]
			obstacleGroup.add(Obstacle(self.formatPickleToSurface(pickledObs[0]),pickledObs[1],pickledObs[2],self.elements['BoardStep']))
			obsPtr = obsPtr + 1
		return obstacleGroup
		
	def setBeeBotHeading(self,input):
		self.elements['BeeBotHeading'] = input

	def getBeeBotHeading(self):
		return self.elements['BeeBotHeading']
		
	def setBeeBotSprite(self,inputString):
		input = pygame.image.load(inputString)
		self.elements['BeeBotSprite'] = self.formatSurfaceForPickle(input)
		
	def getBeeBotSprite(self):
		return self.formatPickleToSurface(self.elements['BeeBotSprite'])
		
	def getBeeBotStartPosition(self):
		return self.elements['BeeBotStartPosition']
		
	def setBeeBotStartPosition(self,x,y):
		self.elements['BeeBotStartPosition'] = (x,y)
	
	def getLogicalHeight(self):
		return self.elements['LogicalHeight']
		
	def getLogicalWidth(self):
		return self.elements['LogicalWidth']	

	def setLogicalHeight(self,input):
		self.elements['LogicalHeight'] = input
		
	def setLogicalWidth(self,input):
		self.elements['LogicalWidth'] = input
		
	def getBoardStep(self):
		return self.elements['BoardStep']
		
	def setBoardStep(self,input):
		self.elements['BoardStep'] = input
	
	def formatPickleToSurface(self,input):
		if input == None:
			return None
		return pygame.image.fromstring(input['image'],input['size'],input['format'])
	
	def formatSurfaceForPickle(self,input):
		if input == None:
			return None
		return {'image': pygame.image.tostring(input,"RGBA"), 'size': input.get_size(), 'format': "RGBA"}
		
	def setBackground(self,inputString):
		input = pygame.image.load(inputString)
		self.elements['Background'] = self.formatSurfaceForPickle(input)
		
	def getBackground(self):
		return self.formatPickleToSurface(self.elements['Background'])
		
	def setBorderColour(self,input):
		self.elements['BorderColour'] = input
	
	def getBorderColour(self):
		return self.elements['BorderColour']
	
	def getName(self):
		return self.elements['Name']
	
	def writeToFile(self):
		pickle.dump( self, open( "./scenarios/"+ self.name +".scibot", "wb" ) )