import pygame
from src.Scenario import *
from src.BeeBot import Heading
from src.Obstacle import *

#initalises a new scenario object and sets the scenario name. Currently the name does nothing
s = Scenario("Default")

#the size of an individual square
s.set_board_step(150)

#sets the width of the map in terms of squares
s.set_logical_width(5)
#sets the height of the map in terms of squares
s.set_logical_height(8)

#the dimensions of the image must match up exactly with how the map is represented in the program, ie the image width must be BoardStep * LogicalWidth

#sets the bee bot starting square (x,y)
s.set_beebot_start_position(3,1)
#set the beebot sprite
s.set_beebot_sprite("./img/Default/robot.jpg")
#sets the beebots starting direction, where "UP" is "Heading.NORTH", other options are Heading.East etc
s.set_beebot_heading(Heading.NORTH)

#sets the image on the map
s.set_background("./img/Default/background.jpg")
#if the image has no grid, one can be added by choosing a coulour for the lines below
border_colour = (0,0,255)
s.set_border_colour(border_colour)

#this line addes an obstacle at square (2,1) with sprite "./img/Default/obstacle1.jpg".
#s.addObstacle(2,1) addes an obstacle at (2,1) with no sprite, ie it will show whatever is on the background
s.add_obstacle(2,1,"./img/Default/obstacle1.jpg")
#this line addes an obstacle at square (2,3) with sprite "./img/Default/obstacle1.jpg".
s.add_obstacle(2,3,"./img/Default/obstacle1.jpg")


#adds an goal square at (1,2) with sprite "./img/Default/goal1.jpg"
s.add_goal(1,2,"./img/Default/goal1.jpg")
#again, s.addGoal(1,2) would add a spriteless goal at (1,2)
s.add_goal(2,0,"./img/Default/goal1.jpg")

#sets the sprite to be displayed when the robot crashes
s.set_beebot_fail_sprite("./img/Default/robotx.jpg")

s.write_to_file()
