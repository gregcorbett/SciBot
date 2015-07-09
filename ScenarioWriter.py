import pygame
from src.Scenario import *

s = Scenario("Default")

background = "./img/background.jpg"
borderColour = (0,0,255)

s.setBackground(background)
s.setBorderColour(borderColour)

#obstacleGroup = {}

o1 = Obstacle("./img/obstacle1.jpg",4,2,self)
o2 = Obstacle("./img/obstacle1.jpg",6,2,self)
		
#obstacleGroup.add(o1)
#obstacleGroup.add(o2)

s.writeToFile()
