import pygame
from src.Scenario import *

s = Scenario("Default")

background = pygame.image.load("./img/background.jpg")

s.setBackground(background)

s.writeToFile()
