import pygame
from src.Scenario import *

s = Scenario("Default")

background = pygame.image.load("./img/background.jpg")
borderColour = (0,0,255)

s.setBackground(background)
s.setBorderColour(borderColour)




s.writeToFile()
