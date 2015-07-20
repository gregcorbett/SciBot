import pygame
from src.Scenario import *
from src.BeeBot import Heading
from src.Obstacle import *

s = Scenario("Default")

s.setBoardStep(150)
s.setLogicalWidth(5)
s.setLogicalHeight(8)

s.setBeeBotStartPosition(3,1)
s.setBeeBotSprite("./img/Default/robot.jpg")
s.setBeeBotHeading(Heading.NORTH)

borderColour = (0,0,255)

s.setBackground("./img/Default/background.jpg")
s.setBorderColour(borderColour)

s.addObstacle(2,1,"./img/Default/obstacle1.jpg")
s.addObstacle(2,3,"./img/Default/obstacle1.jpg")

s.addGoal(1,2,"./img/Default/goal1.jpg")
s.addGoal(2,0,"./img/Default/goal1.jpg")

s.setBeeBotFailSprite("./img/Default/robotx.jpg")
		
s.writeToFile()
