import pygame
from src.Scenario import *
from src.BeeBot import Heading
from src.Obstacle import *

s = Scenario("Default")

s.setBoardStep(150)
s.setLogicalWidth(5)
s.setLogicalHeight(8)

s.setBeeBotStartPosition(3,1)
s.setBeeBotSprite("./img/robot.jpg")
s.setBeeBotHeading(Heading.NORTH)

borderColour = (0,0,255)

s.setBackground("./img/background.jpg")
s.setBorderColour(borderColour)

s.addObstacle("./img/obstacle1.jpg",2,1)
s.addObstacle("./img/obstacle1.jpg",2,3)

s.addGoal("./img/goal1.jpg",1,2)
s.addGoal("./img/goal1.jpg",2,0)

s.setBeeBotFailSprite("./img/robotx.jpg")
		
s.writeToFile()
