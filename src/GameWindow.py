import pygame
import time
import threading
import pickle

from src.BeeBot import *
from src.Board import *
from src.CustomEvent import *
from src.Scenario import *

class GameWindow():#threading.Thread):
	def __init__(self):
		pygame.init()
		
	def chooseScenario(self):
		self.scenario = None
		#Somehow choose a scenario
		
		self.scenario = "UV"
		
		if self.scenario == None:
			self.scenario = "Default"
		
		self.scenario = pickle.load( open( "../scenarios/" + self.scenario + ".scibot", "rb" ) )
	
	def loadScenario(self):
		#	super(GameWindow,self).__init__()
		
		self.step = self.scenario.getBoardStep()
		self.height = self.scenario.getLogicalHeight()*self.step
		self.width = self.scenario.getLogicalWidth()*self.step
		
		self.board = Board(self.scenario.getLogicalWidth(),self.scenario.getLogicalHeight(),self.step,self.scenario)
		self.size = (self.width,self.height)
		
		self.robot = BeeBot(self.board,self.scenario)
		
		self.screen = pygame.display.set_mode(self.size) 
		
		self.display()
		
		self.clock = pygame.time.Clock()
			
	def startScenario(self):
		
		#pygame.event.set_allowed([])
		#pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT])
		
		while True:
			#pygame.event.pump()
			event = pygame.event.poll()
			
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == CustomEvent.RUN_FAIL:
				pygame.quit()
				sys.exit()

			if event.type == CustomEvent.RUN_WIN:
				print("YOU WIN!!!")
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_UP))
				if event.key == pygame.K_DOWN:
					self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_DOWN))
				if event.key == pygame.K_LEFT:
					self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_LEFT))
				if event.key == pygame.K_RIGHT:
					self.robot.addToMemory(pygame.event.Event(CustomEvent.MOVE_BEEBOT_RIGHT))
				if event.key == ord('g') or event.key == ord('G'):
						self.robot.pushOutMemory()
						
			if event.type >= CustomEvent.MOVE_BEEBOT_UP and event.type <= CustomEvent.MOVE_BEEBOT_RIGHT:
				self.robot.move(event,self.screen)
				self.checkForObstacleCollisions()
				self.checkForGoalCollisions()
				
			#newEvent = pygame.event.Event(Direction.LEFT)
			#print(newEvent.type)
			#pygame.quit()
			#sys.exit()
			
			self.display()
			pygame.display.update()
			self.clock.tick(30)
			
	
	def checkForGoalCollisions(self):
		currentGoal = self.board.goalGroup.goals[self.board.goalGroup.goalPtr]
		if self.robot.logicalPositionX == currentGoal.logicalPositionX and self.robot.logicalPositionY == currentGoal.logicalPositionY:
			self.board.goalGroup.goalPtr = self.board.goalGroup.goalPtr + 1
			if self.board.goalGroup.goalPtr == self.board.goalGroup.goalCount:
				#final goal
				pygame.event.clear()
				pygame.event.post(pygame.event.Event(CustomEvent.RUN_WIN))
				
	def checkForObstacleCollisions(self):
		obsPtr = 0
		while obsPtr < self.board.obstacleGroup.obstacleCount:
			obs = self.board.obstacleGroup.obstacles[obsPtr]
			if self.robot.logicalPositionX == obs.logicalPositionX and self.robot.logicalPositionY == obs.logicalPositionY:
				self.robot.sprite = self.robot.failSprite
				pygame.event.clear()
				pygame.event.post(pygame.event.Event(CustomEvent.RUN_FAIL))
			obsPtr = obsPtr + 1
			
	def display(self):
		self.board.display(self.screen)
		self.robot.display(self.screen)
	
	#def run(self):
	#		clock = pygame.time.Clock()
	#		while True:
	#			self.board.display(self.screen)
	#			self.robot.display(self.screen)
	#			pygame.display.update()
				#time.sleep(0.2)
				#clock.tick(30)