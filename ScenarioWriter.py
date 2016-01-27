import pygame
from src.Scenario import *
from src.BeeBot import Heading
from src.Obstacle import *

#initalises a new scenario object and sets the scenario name. Currently the name does nothing
s = Scenario("Default")

#the size of an individual square
s.setBoardStep(150)

#sets the width of the map in terms of squares
s.setLogicalWidth(5)
#sets the height of the map in terms of squares
s.setLogicalHeight(8)

#the dimensions of the image must match up exactly with how the map is represented in the program, ie the image width must be BoardStep * LogicalWidth

#sets the bee bot starting square (x,y) 
s.setBeeBotStartPosition(3,1)
#set the beebot sprite
s.setBeeBotSprite("./img/Default/robot.jpg")
#sets the beebots starting direction, where "UP" is "Heading.NORTH", other options are Heading.East etc
s.setBeeBotHeading(Heading.NORTH)

#sets the image on the map
s.setBackground("./img/Default/background.jpg")
#if the image has no grid, one can be added by choosing a coulour for the lines below
borderColour = (0,0,255)
s.setBorderColour(borderColour)

#this line addes an obstacle at square (2,1) with sprite "./img/Default/obstacle1.jpg". 
#s.addObstacle(2,1) addes an obstacle at (2,1) with no sprite, ie it will show whatever is on the background
s.addObstacle(2,1,"./img/Default/obstacle1.jpg")
#this line addes an obstacle at square (2,3) with sprite "./img/Default/obstacle1.jpg".
s.addObstacle(2,3,"./img/Default/obstacle1.jpg")

#this line adds an goal square at (1,2) with sprite "./img/Default/goal1.jpg"
#again, s.addGoal(1,2) would add a spriteless goal at (1,2)
s.addGoal(1,2,"./img/Default/goal1.jpg")
#currently, goals must be reached by the beebot in the order they are added
s.addGoal(2,0,"./img/Default/goal1.jpg")

#sets the sprite to be displayed when the robot crashes
s.setBeeBotFailSprite("./img/Default/robotx.jpg")
		
s.writeToFile()
