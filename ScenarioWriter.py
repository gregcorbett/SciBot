import pygame
from src.Scenario import *
from src.BeeBot import Heading

s = Scenario("Default")

s.setBoardStep(150)
s.setLogicalWidth(5)
s.setLogicalHeight(8)

s.setBeeBotStartPosition((3,6))
s.setBeeBotSprite("./img/robot.jpg")
s.setBeeBotHeading(Heading.NORTH)

borderColour = (0,0,255)

s.setBackground("./img/background.jpg")
s.setBorderColour(borderColour)

#obstacleGroup = {}

#o1 = Obstacle("./img/obstacle1.jpg",4,2,self)
#o2 = Obstacle("./img/obstacle1.jpg",6,2,self)
		
#obstacleGroup.add(o1)
#obstacleGroup.add(o2)

s.writeToFile()
