import pygame
import time

class Board:
	def __init__(self):
		#from VideoCapture import Device
		pygame.init()
		w = 640
		h = 480
		size=(w,h)
		screen = pygame.display.set_mode(size) 
		#c = pygame.time.Clock() # create a clock object for timing

		#cam = Device()
		#filename = str(In)+".jpg" # ensure filename is correct
		#cam.saveSnapshot(filename) 
		img=pygame.image.load("./img/background.jpg") 
		screen.blit(img,(0,0))
		pygame.display.flip() # update the display
		#c.tick(3) # only three images per second